Research
====================
I got into research as an undergraduate at UC Davis with [Prof. Tripathi](https://physics.ucdavis.edu/people/faculty/sudhindra-tripathi), working on simulation software for the [LUX dark matter detector](https://sites.brown.edu/luxdarkmatter/experiment/).  My senior thesis work sped up the simulation significantly by bypassing photon propagation calculations, instead probabilistically distributing them to the various detectors based on the position they were generated.  This work contributed to **@Szydagis2013** and established a strong computational theme to my research interests.

In graduate school at UCSC, I worked on connecting giant planet physics with their observed properties with my advisor [Jonathan Fortney](https://jfortney.sites.ucsc.edu/).  This work branched into a variety of related topics extending into my postdoctoral work, so I'll organize them that way rather than strictly by date.  This research principally relies on planetary interior structure models and Bayesian statistics.

Note: Articles on which I am an author are bolded.

Giant Planet Compositions
--------------------
<a href="massMetal.png"><img src="massMetal.png" id="sideimg"/></a>

Among giant exoplanets, those with equilibrium temperatures below 1000 K have radii that are well explained by the same interior structure models that were developed for Jupiter and Saturn.  As such, we can infer their bulk compositions by adjusting the parameter in structure models such that radius matches its observed value.  I did this for 47 giant planets, finding that the bulk metal mass was related to the mass as approximately $M_z \propto M^{0.61}$ **[@Thorngren2016]**.  Since the bulk metallicity is the mass fraction $Z=M_z/M$, this means metallicity is negatively correlated by mass.  This scaling resembles that of mass of solids in the protoplanetary disk within the gravitational influence of the planet during formation, suggesting that this late accretion of solids plays an important role in determining final compositions.  It also implies that these planets will typically have low C/O ratios in their atmospheres **[@Espinoza2017]**.

Bulk compositions also have value in support of atmospheric observations; especially transmission and emission spectroscopy.  The atmospheric metallicity cannot exceed the bulk metallicity stably **[@Thorngren2019]**; allowing the latter to serve as an easily-obtained upper-limit on the plausible atmospheric metallicity **[@Kreidberg2018; @Mikal-Evans2021; @Baxter2021; @Bean2023]**.  With the successful launch and commissioning of the James Webb Space Telescope (JWST), we have been able to go further.  If an upper-limit on the atmospheric metallicity can be established, then knowing the bulk metallicity sets a *lower limit* on the core mass of the planet **[@Sing2024]**, including any "fuzzy" core layers [@Bloot2023].  This is an exciting new frontier in exoplanet science, as the core mass corresponds to the mass during formation at which the planet was able to retain large quantities of H/He, beginning runaway accretion [@Helled2017].

Hot Jupiter Heating
--------------------
<a href="fluxRadius.png"><img src="fluxRadius.png" id="sideimg"/></a>

Hot Jupiters; defined for this purpose as those with equilibrium temperatures *above* 1000 K, are unexpectedly large compared to our models.  My review chapter, **@Thorngren2024** (figure right), covers some of the history and current state of this problem.  While we have made a great deal of progress in understanding the effect, the problem has not yet been resolved.

A key part of the challenge is that for these planets, both the internal temperatures and the composition are not known, preventing us from inferring either directly from the radius.  My contribution to this area was **@Thorngren2018**, in which I used a hierarchical Bayesian model that identified the internal temperatures that would correspond to these planets having the same distribution of compositions seen for the warm giants **[@Thorngren2016]**.  Modeling this as a single source of additional heat deep within the planet, we found that it peaks as a fraction if the incoming light energy at $T_\mathrm{eq} \approx 1600$ K.  This matches predictions for the Ohmic dissipation explanation [@Menou2012], as a result of a strong dependence on the atmospheric wind speeds, which feature that same peak.  However, it could also support other processes that depend on the wind speed, like temperature advection [@Tremblin2017].

This heating has important implications for other aspects of hot Jupiter physics.  First, it suggests that their intrinsic temperatures (a measure of heat rising from the interior) is *much* higher **[@Thorngren2019b]** than the 100 K of Jupiter, which in turn pushes their radiative convective boundaries to higher altitudes / lower pressures.  This is an important input for global circulation models **[@Komacek2022]**, and affects the pressure-temperature profile, cloud structure **[@Gao2020]**, and disequilibrium chemistry **[@Fortney2020]** as well.  Finally, a larger intrinsic flux could allow for a very strong magnetic field **[@Yadav2017]**, though this would depend on the location and nature of the magnetic dynamo.

The age-dependence of hot Jupiter radii, can tell us about the process that heats them as well; [@Lopez2016] observe that when $T_\mathrm{eq}$ increases, whether the planet grows larger (reinflates) depends on whether the effect is heat trapping or active heating of the interior.  A number of papers have followed up on this; for my part, I observed in **[@Thorngren2021]** that hot Jupiters orbiting main-sequence stars show evidence of *both* heat trapping and active heating.

<hr>
