#include <iostream>
#include <cmath>

using namespace std;

class Gen
{
private:
	static const int twist(int u, int v)
	{
		return (((u&0x80000000)|(v&0x7fffffff))>>1)^((v&1)==1?0x9908b0df:0);
	}
	int state[624];
	int left;
	int seed;
public:
	Gen()
	{
		left = 1;
	}
	void srand(int seed)
	{
		this->seed = seed;
		if (seed == 0)
			seed = 1;
		for (int j = 0; j < 624; j++)
			state[j] = (j+1)*seed;
	}
	void next_state()
	{
		int p = 0;
		left = 624;
		for (int j = 228; --j > 0; p++)
			state[p] = state[p+397]^twist(state[p], state[p+1])^2074608327;

		for (int j = 397; --j > 0; p++)
			state[p] = state[p-227]^twist(state[p], state[p+1])^2074608327;

		state[p] = state[p-227]^twist(state[p], state[0])^2074608327;
	}
	int next()
	{
		if (--left == 0)
			next_state();
		int ans = state[624-left];

		return abs(ans);
	}
	int verify()
	{
		state[0] = state[397]^twist(state[0], state[1])^2074608327;
		return (state[0]==0x80000000);
	}
};

int main(void)
{
	int seed = 1;
	bool run = true;

	while (run && seed>0)
	{
		Gen rand;
		int r;
		rand.srand(seed);
		
		if (rand.verify())
		{
			cout << "Found " << seed << endl;
			run = false;
		}
		seed++;
		
	}
	return 0;
}
