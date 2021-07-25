
import itertools
import numpy as np

if __name__ == "__main__":
    import general
else:
    from . import general

class ProbDist:
    def __init__(self, **kwargs) -> None:
        if (state_probs := kwargs.get('state_probs')) and (type(state_probs) == list or type(state_probs) == tuple):
            # no probabilities were given, so default to even distribution
            state_probs = {state:(1/len(state_probs)) for state in state_probs}
        else: # probabilities were given
            assert (type(state_probs) == dict), "state_probs must be a dictionary state:prob"
            temp = sum(list(state_probs.values()))
            if temp - 1 > 0.0000000000001: # arbitrary boi to handle precision issues
                raise Exception(f"Probs must sum to 1, not {temp}")
        self.state_probs = state_probs
        self.func = kwargs.get('func')
        if kwargs.get('debug'):
            print(self)
    def __str__(self) -> str:
        return '\n'.join([f"{s}"+"\t{:0.3f}%".format(100*p) for s,p in self.state_probs.items()])
    def __mul__(self, other):
        new_state_probs = {}
        for si, sj in itertools.product(list(self.state_probs.keys()), list(other.state_probs.keys())):
            new_state = general.tuplify(si, sj)
            if self.func != None:
                new_state = self.func(new_state)
            new_prob = self.state_probs[si] * other.state_probs[sj]
            assert (new_prob <= 1.0), "Something definitely went wrong here"
            if new_state not in new_state_probs:
                new_state_probs[new_state] = 0
            new_state_probs[new_state] += new_prob
        return ProbDist(state_probs=new_state_probs, func=self.func)
    def events(self):
        return self.state_probs.keys()
    def prob(self, state):
        return self.state_probs.get(state) or 0.0
    def probs(self):
        return self.state_probs.items()
    def probs_error(self):
        return 1.0 - sum(self.probs.values())
    def asMatrix(self, ordering, **kwargs):
        asRow = kwargs.get("asRow") # default = False
        sparse = kwargs.get("sparse") # default = False
        m = np.zeros(shape=((1,len(ordering)) if asRow else (len(ordering),1)))
        def set_element(i, e):
            if asRow:
                m[0,i] = e
            else:
                m[i,0] = e 
        if sparse: # events in ordering don't need to match self.state_probs at all
            for i, x in enumerate(ordering):
                set_element(i, self.prob(x))
        else: # Catch ordering errors
            if len(ordering) != len(self.state_probs):
                raise Exception(f"Invalid ordering length! {len(ordering)}, {len(self.state_probs)}")
            if len(ordering) != len(set(ordering)):
                raise Exception(f"Invalid ordering! Cannot contain duplicates")
            for i, key in enumerate(ordering):
                set_element(i, self.state_probs[key])
        return m

