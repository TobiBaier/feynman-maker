import numpy as np
"""
theoretical random pairing algorithm:
 1) all external particles (i/o) are matched with one of the intermediary node ports
 2) all remaining intermediary nodes are matched with each other
 3) 
"""

"""
MORE RELEVANT FOR LATER PROGRAMS

particle identifiers? -> might be able to get way with assigning exact particle names later on -> graph theory
 -> needs: type (fermion, boson), (no) anti, interaction types? 
 -> somehow discriminate, that e.g. neutrinos can only interact weakly? -> some sort of <ioi> String with i=yes, o=no?
        -> positional coding for qed, qcd, weak, higgs (basically boson type)

 -> i suppose maybe you can generate all combinations and eliminate the ones not allowed afterwards?
    -> might save calculation time if you already do it while pairing up?
    -> this would need a BUNCH of information though, especially for more complex vertices later on
    -> might be the best approach though, as it allows for easier modification of the model, because it makes it
       easy to add new particles and interaction rules

possible identifier:
 <type><anti><interactions>
 possible identifiers:
    <type>: f, b
    <anti>: n, a
    <interaction>: y/ny/ny/ny/n     for qed, qcd, weak, higgs
"""

"""
only qed for now
 - 3 needed identifiers -> fermion/boson, normal/anti, name
 
 electron: fn_electron
 antielectrom: fa_antielectron 
 

"""



"""input_list = ["f1", "f2", "p1", "p2", "q1f1", "q1f2", "q1p1", "q2f1", "q2f2", "q2p1", ]

in_list = ["f1", "f2"]
inter_list = ["q1f1", "q1f2", "q1p1", "q2f1", "q2f2", "q2p1"]
out_list = ["p1", "p2"]"""

# example process: Bhabha-scattering: e+e- -> e+e-

external = ["fa4e", "fn3e", "fn2e", "fa1e"]

internal = ["f1q1", "f2q1", "p1q1", "f1q1", "f2q1", "p1q1", ]





result = {
    "f1": "q1f1",
    "f2": "q2f1",
}





