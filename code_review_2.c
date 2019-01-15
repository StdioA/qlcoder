// PHP trim 和 is_numeric 源代码

PHPAPI char *php_trim(char *c, int len, char *what, int what_len, zval *return_value, int mode TSRMLS_DC)
{
    register int i;
    int trimmed = 0;
    char mask[256];

    if (what) {
        php_charmask((unsigned char*)what, what_len, mask TSRMLS_CC);
    } else {
        php_charmask((unsigned char*)" \n\r\t\v\0", 6, mask TSRMLS_CC);
    }
        //从左开始
    if (mode & 1) {
        for (i = 0; i < len; i++) {
            if (mask[(unsigned char)c[i]]) {        //该位置有第二个参数对应的值
                trimmed++;
            } else {
                break;
            }
        }
        len -= trimmed;
        c += trimmed;
    }
    if (mode & 2) {
        for (i = len - 1; i >= 0; i--) {
            if (mask[(unsigned char)c[i]]) {
                len--;
            } else {
                break;
            }
        }
    }

    if (return_value) {
                //把c指针现在指向的位置以后的len个字符返回
        RETVAL_STRINGL(c, len, 1);
    } else {
        return estrndup(c, len);
    }
    return "";
}


static inline zend_uchar is_numeric_string_ex(const char *str, int length, long *lval, double *dval, int allow_errors, int *oflow_info)
{
    const char *ptr;
    int base = 10, digits = 0, dp_or_e = 0;
    double local_dval = 0.0;
    zend_uchar type;

    if (!length) {
        return 0;
    }

    if (oflow_info != NULL) {
        *oflow_info = 0;
    }

    /* Skip any whitespace
     * This is much faster than the isspace() function */
    while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\r' || *str == '\v' || *str == '\f') {
        str++;
        length--;
    }
    ptr = str;

    if (*ptr == '-' || *ptr == '+') {
        ptr++;
    }

    if (ZEND_IS_DIGIT(*ptr)) {
        /* Handle hex numbers
         * str is used instead of ptr to disallow signs and keep old behavior */
        if (length > 2 && *str == '0' && (str[1] == 'x' || str[1] == 'X')) {
            base = 16;
            ptr += 2;
        }

        /* Skip any leading 0s */
        while (*ptr == '0') {
            ptr++;
        }

        /* Count the number of digits. If a decimal point/exponent is found,
         * it's a double. Otherwise, if there's a dval or no need to check for
         * a full match, stop when there are too many digits for a long */
        for (type = IS_LONG; !(digits >= MAX_LENGTH_OF_LONG && (dval || allow_errors == 1)); digits++, ptr++) {
check_digits:
            if (ZEND_IS_DIGIT(*ptr) || (base == 16 && ZEND_IS_XDIGIT(*ptr))) {
                continue;
            } else if (base == 10) {
                if (*ptr == '.' && dp_or_e < 1) {
                    goto process_double;
                } else if ((*ptr == 'e' || *ptr == 'E') && dp_or_e < 2) {
                    const char *e = ptr + 1;

                    if (*e == '-' || *e == '+') {
                        ptr = e++;
                    }
                    if (ZEND_IS_DIGIT(*e)) {
                        goto process_double;
                    }
                }
            }

            break;
        }

        if (base == 10) {
            if (digits >= MAX_LENGTH_OF_LONG) {
                if (oflow_info != NULL) {
                    *oflow_info = *str == '-' ? -1 : 1;
                }
                dp_or_e = -1;
                goto process_double;
            }
        } else if (!(digits < SIZEOF_LONG * 2 || (digits == SIZEOF_LONG * 2 && ptr[-digits] <= '7'))) {
            if (dval) {
                local_dval = zend_hex_strtod(str, &ptr);
            }
            if (oflow_info != NULL) {
                *oflow_info = 1;
            }
            type = IS_DOUBLE;
        }
    } else if (*ptr == '.' && ZEND_IS_DIGIT(ptr[1])) {
process_double:
        type = IS_DOUBLE;

        /* If there's a dval, do the conversion; else continue checking
         * the digits if we need to check for a full match */
        if (dval) {
            local_dval = zend_strtod(str, &ptr);
        } else if (allow_errors != 1 && dp_or_e != -1) {
            dp_or_e = (*ptr++ == '.') ? 1 : 2;
            goto check_digits;
        }
    } else {
        return 0;
    }

    if (ptr != str + length) {
        if (!allow_errors) {
            return 0;
        }
        if (allow_errors == -1) {
            zend_error(E_NOTICE, "A non well formed numeric value encountered");
        }
    }

    if (type == IS_LONG) {
        if (digits == MAX_LENGTH_OF_LONG - 1) {
            int cmp = strcmp(&ptr[-digits], long_min_digits);

            if (!(cmp < 0 || (cmp == 0 && *str == '-'))) {
                if (dval) {
                    *dval = zend_strtod(str, NULL);
                }
                if (oflow_info != NULL) {
                    *oflow_info = *str == '-' ? -1 : 1;
                }

                return IS_DOUBLE;
            }
        }

        if (lval) {
            *lval = strtol(str, NULL, base);
        }

        return IS_LONG;
    } else {
        if (dval) {
            *dval = local_dval;
        }

        return IS_DOUBLE;
    }
}
