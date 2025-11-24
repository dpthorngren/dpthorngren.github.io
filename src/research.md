---
pagetitle: Research -- D.P. Thorngren
author: D.P. Thorngren
lang: en-US
link-citations: True
---

Research
====================
Since a complete list of my publications can be found on the [NASA/SAO ADS](https://ui.adsabs.harvard.edu/search/q=Thorngren%2C%20Daniel%20property%3Arefereed) as well as my [CV](thorngrenCV.pdf), I'll organize this page by research topic rather than date or number of citations.  Papers on which I am an author are **bolded**, and the bibliography at the bottom of this page links to the papers themselves.  This is not a full review, so not all relevant papers are cited; for that I'd recommend traversing the citation graph on the ADS.

Giant Planet Compositions
--------------------
[![Mass-metallicity relation](massMetal.png){id="sideimg"}](massMetal.png)

Giant exoplanets with equilibrium temperatures below 1000 K have radii that are well explained by the same interior structure models that were developed for Jupiter and Saturn.  As such, we can infer their bulk compositions by adjusting the parameter in structure models such that radius matches its observed value.  I did this for 47 giant planets, finding that the bulk metal mass was related to the mass as approximately $M_z \propto M^{0.61}$ **[@Thorngren2016]**.  Since the bulk metallicity is the mass fraction $Z=M_z/M$, this means metallicity is negatively correlated by mass.

This scaling resembles that of mass of solids in the protoplanetary disk within the gravitational influence of the planet during formation, suggesting that this late accretion of solids plays an important role in determining final compositions.  It also implies that these planets will typically have low C/O ratios in their atmospheres **[@Espinoza2017]**.  While core-accretion models might suggest linear relationship between stellar and planetary metallicities, comparisons with stellar metallicities indicate the relationship is much weaker than that **[@Teske2019; @Thorngren2021]**, perhaps as a result of the chaotic nature of planet formation.

Bulk compositions also have value in support of atmospheric observations, especially transmission and emission spectroscopy.  The atmospheric metallicity cannot exceed the bulk metallicity stably **[@Thorngren2019]**, allowing the latter to serve as an easily-obtained upper-limit on the plausible atmospheric metallicity **[@Kreidberg2018; @Mikal-Evans2021; @Baxter2021; @Bean2023]**.

With the successful launch and commissioning of the James Webb Space Telescope (JWST), we have been able to go further.  If an upper-limit on the atmospheric metallicity can be established, then knowing the bulk metallicity sets a *lower limit* on the core mass of the planet **[@Sing2024]**, including any "fuzzy" core layers [@Bloot2023].  This is an exciting new frontier in exoplanet science, as the core mass corresponds to the mass during formation at which the planet was able to retain large quantities of H/He, beginning runaway accretion [@Helled2017].

Hot Jupiter Heating
--------------------
[![Flux-radius diagram.](fluxRadius.png){id="sideimg"}](fluxRadius.png)

Hot Jupiters, defined for this purpose as those with equilibrium temperatures *above* 1000 K, are unexpectedly large compared to our models.  My review chapter, **@Thorngren2024** (figure right), covers some of the history and current state of this problem.  While we have made a great deal of progress in understanding the effect, the problem has not yet been resolved.

A key part of the challenge is that for these planets, both the internal temperatures and the composition are not known, preventing us from inferring either directly from the radius.  My contribution to this area was **@Thorngren2018**, in which I used a hierarchical Bayesian model that identified the internal temperatures that would correspond to these planets having the same distribution of compositions seen for the warm giants **[@Thorngren2016]**.  Modeling this as a single source of additional heat deep within the planet, we found that it peaks as a fraction if the incoming light energy at $T_\mathrm{eq} \approx 1600$ K.  This matches predictions for the Ohmic dissipation explanation [@Menou2012], as a result of a strong dependence on the atmospheric wind speeds, which feature that same peak.  However, it could also support other processes that depend on the wind speed, like temperature advection [@Tremblin2017].

This heating has important implications for other aspects of hot Jupiter physics.  First, it suggests that their intrinsic temperatures (a measure of heat rising from the interior) is *much* higher **[@Thorngren2019b]** than the 100 K of Jupiter, which in turn pushes their radiative convective boundaries to higher altitudes / lower pressures.  This is an important input for global circulation models **[@Komacek2022]**, and affects the pressure-temperature profile, cloud structure **[@Gao2020]**, and disequilibrium chemistry **[@Fortney2020]** as well.  Finally, a larger intrinsic flux could allow for a very strong magnetic field **[@Yadav2017]**, though this would depend on the location and nature of the magnetic dynamo.

The age-dependence of hot Jupiter radii, can tell us about the process that heats them as well: [@Lopez2016] observe that when $T_\mathrm{eq}$ increases, whether the planet grows larger (reinflates) depends on whether the effect is heat trapping or active heating of the interior.  A number of papers have followed up on this; for my part, I observed in **[@Thorngren2021]** that hot Jupiters orbiting main-sequence stars show evidence of *both* heat trapping and active heating.

Mass Loss and Tidal Evolution
--------------------
Tides and XUV-driven mass loss were a natural area for my research to branch out in, as they are both driven by the radius and affect the interior evolution of the planet.  For example, XUV-driven mass loss rates scale as the radius *cubed*, but losing mass can change the radius of the planet.  In **@Thorngren2023** I found that this results in a feedback loops for hot Saturns which, under the right conditions, can remove large portions of a planet's gaseous envelope.

This experience, along with my more standard interior structure models, has allowed me to contribute to a number of projects on the fascinating case of super-puffs **[@Yoshida2023; @Vissapragada2024; @Thao2024; @Karalis2025; @Yee2025]**.  These planets have both puzzlingly large radii for their low masses (hence the name) and appear to push the boundaries of gaseous planet stability.  It remains unclear whether this is due to low metallicity or high temperatures, as either result is surprising.

Tidal evolution is related in a couple of ways.  First, the mass loss process itself can push a planet into higher orbits [@Valsecchi2014], which we considered in **@Thorngren2023**.  Second, eccentric planets can undergo tidal circularization, which reduces the semimajor axis and eccentricity while heating the planetary interior, enlarging it.  This may help to explain some warm, low-density planets **[@Morley2017; @Dang2022; @Piaulet2023; @Sing2024]**.  Finally, in the most extreme cases **[@Wahl2021]**, the tides of a star on a planet can pull it into a prolate ellipsoid shape (somewhat like a football or egg).

Astrostatistics
--------------------
While many of the aforementioned projects have had a strong statistical component **[@Thorngren2018; @Thorngren2021]**, there are others for which the statistics were my primary contribution.  **@Movshovitz2020** explored the space of Saturn interior structures consistent with the data, while not incorporating any equations of state *a priori*; my involvement was mainly helping to properly sampling the quite challenging posterior distribution.  In **@Mayorga2020**, I helped to design the statistical model and wrote the core code used to fit them to the data.

[![Sigma Comparison](sigma_comparison.png){id="sideimg"}](sigma_comparison.png)

More recently, in **@Thorngren2025** I observed that a statistical technique widely used in exoplanet atmospheres was invalid.  The error was based on a misunderstanding of @Sellke2001, which gave a way to interpret the p-values of simple hypotheses as an upper limit on the Bayes factor.  Astronomers were using this to obtain an upper limit on the p-value from their Bayes factors, but this violated the requirements of the original formula and generally overestimates the confidence compared to proper significance tests.  The figure on the right shows a comparison; the erroneous method is in orange and the standard Bayesian approach is in blue.  I also discussed the prior sensitivity of Bayes factor analyses, and suggest the use of the simplified Bayesian predictive information criterion (BPICS, @Ando2011) as a less prior-sensitive supporting test.

<hr>
