# Cost Constrained Network Growth

MATLAB code for modeling the growth of a simple binary network based on the ecological growth model described in:

Simple mathematical models with very complicated dynamics. 

Nature 261 459-67, (1976)

Abstract:

_First-order difference equations arise in many contexts in the biological, economic, and social sciences. Such equations, even though simple and deterministic, can exhibit a suprising array of dynamical behaviour, from stable points, to a bifuricating hierarchy of stable cycles, to apparently random fluctuations. There are consequently many fascinating problems, some concerned with the practical implications and applications, This is an interpretive review of them._


This paper talks in detail about the "logistic" difference equation, which is, in it's canonical form:

_X<sub>t+1</sub> = aX<sub>t</sub>(1-X<sub>t</sub>)_

Within this equation, _X_ is the current population size as a fraction of the largest possible population. _X_ is required to remain on the interval _0<X<1_. If _X_ ever exceeds unity, subsequant iterations of the model converge to - \infty (which would result in extinction of the population). The value of _a_ is the combined birth/death rate of the population. For non-trivial dynamic behaviour, it is required that _1<a<4_, otherise the population will become extinct.

Here, we have a applied this population growth model to the growth of nodes and edges within a complex network.The growth of nodes is modeled with a fixed cap, maximum, number of nodes the network can grow to, and _X_ is expressed as a fraction of this. The fraction of maximum edges is based, at each time point, on the current number of nodes within the network.

At each time point, the number of nodes the network increases or decreases by is caluculated, and _then_ the number of edges to add or remove are calculated. New edges are then randomly allocated to nodes. Finaly, any nodes with no edges are removed from the network before completing the iteration. 
