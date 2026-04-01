# Changelog

## [0.2.0](https://github.com/MIT-LCP/croissant-baker/compare/croissant-maker-v0.1.0...croissant-maker-v0.2.0) (2026-04-01)


### Features

* warn on missing Croissant spec-required fields and clarify dev … ([6b1e940](https://github.com/MIT-LCP/croissant-baker/commit/6b1e940bb01e75ecbf9e4e6459fb884a612be645))
* warn on missing Croissant spec-required fields and clarify dev workflow in README ([d65bc56](https://github.com/MIT-LCP/croissant-baker/commit/d65bc56b9df068bc82b82fd650d7d1c65d9c6e22))


### Bug Fixes

* add warning log on skipping malformed image entries in summary ([87dc97e](https://github.com/MIT-LCP/croissant-baker/commit/87dc97e94892c9709b2173de797164a81b73ff68))
* adjust num_images to reflect processed items only in image summary ([7634337](https://github.com/MIT-LCP/croissant-baker/commit/7634337e2c5ff038a1895462356710f0e389e9d0))
* close ParquetFile handle to prevent resource leak ([#54](https://github.com/MIT-LCP/croissant-baker/issues/54)) ([b6240ea](https://github.com/MIT-LCP/croissant-baker/commit/b6240ea2871e658747f108748635ce89cd49212e))
* close ParquetFile handle to prevent resource leak ([#54](https://github.com/MIT-LCP/croissant-baker/issues/54)) ([c6e1caf](https://github.com/MIT-LCP/croissant-baker/commit/c6e1caf6d2ec7bc16f09c3013a203b166e3acd9a))
* resolve KeyError in image_handler properties ([#38](https://github.com/MIT-LCP/croissant-baker/issues/38)) ([494baf2](https://github.com/MIT-LCP/croissant-baker/commit/494baf211fcaed6cf2255b926d1bf31b910d9171))
* resolve KeyError in image_handler properties ([#38](https://github.com/MIT-LCP/croissant-baker/issues/38)) ([ec93a4b](https://github.com/MIT-LCP/croissant-baker/commit/ec93a4b408c7598d2cc4498e031a0812b2351aa8))

## [0.1.0](https://github.com/MIT-LCP/croissant-maker/compare/croissant-maker-v0.0.1...croissant-maker-v0.1.0) (2026-03-27)


### Features

* Add CLI metadata overrides with MIMIC-IV demo example ([b317fc0](https://github.com/MIT-LCP/croissant-maker/commit/b317fc0bdb43652773099726dc526f8fda8d34df))
* Add CLI metadata overrides with MIMIC-IV demo example ([f482c0d](https://github.com/MIT-LCP/croissant-maker/commit/f482c0db281de850d987dec5682003650b9a06d5))
* Add initial Croissant metadata generation CLI ([8b60763](https://github.com/MIT-LCP/croissant-maker/commit/8b60763f7a90149d6b367071be374f1d348fb88c))
* Add initial Croissant metadata generation CLI ([2e552c9](https://github.com/MIT-LCP/croissant-maker/commit/2e552c92783149eb53e10e43a68e7307e3510f1a))
* add MEDS Parquet support and test ([70865ac](https://github.com/MIT-LCP/croissant-maker/commit/70865ac633a5dad04effa13a3b875c973e3f8204))
* add MEDS Parquet support and test ([032a789](https://github.com/MIT-LCP/croissant-maker/commit/032a789cf86fe05ba5ca89c36d285f047d3efd39))
* add MIMIC-IV OMOP test support (closes [#13](https://github.com/MIT-LCP/croissant-maker/issues/13)) ([e7f9a5c](https://github.com/MIT-LCP/croissant-maker/commit/e7f9a5c8ecd5ac914e89c0dd0ad05afdf4064fdd))
* add MIMIC-IV OMOP test support (closes [#13](https://github.com/MIT-LCP/croissant-maker/issues/13)) ([505b27d](https://github.com/MIT-LCP/croissant-maker/commit/505b27d8be26db58823aae75973d9fac8eeb939e))
* CSV streaming + type conflict handling for the full 2 datasets ([0ebed58](https://github.com/MIT-LCP/croissant-maker/commit/0ebed58d5fa7880438e3627dc9496dbbb7e0a027))
* CSV streaming + type conflict handling for the full 2 datasets ([e79370e](https://github.com/MIT-LCP/croissant-maker/commit/e79370e02a75d891868033f207f86be8f1e1d207))
* Make --creator required and add automated testing infrastructure ([e29f9bb](https://github.com/MIT-LCP/croissant-maker/commit/e29f9bbf4de9f4a722f307f9fd7379c5822bb748))
* Make --creator required and add automated testing infrastructure ([8b8ca65](https://github.com/MIT-LCP/croissant-maker/commit/8b8ca651c2902ff2361e9d1a949681bae6e464dc))
* Setup basic project structure ([#1](https://github.com/MIT-LCP/croissant-maker/issues/1)) ([864c853](https://github.com/MIT-LCP/croissant-maker/commit/864c853d06f32b7f5290210a14346416b7863b62))


### Bug Fixes

* add newline at the end of files ([17616b3](https://github.com/MIT-LCP/croissant-maker/commit/17616b3719d59cf38702793d4593353c677bb928))


### Performance Improvements

* fast CSV hashing and opt-in row counting ([70bdfc6](https://github.com/MIT-LCP/croissant-maker/commit/70bdfc68f098b2986b2ef18d28532003af87bfe7))
* fast CSV hashing and opt-in row counting ([1a34e1a](https://github.com/MIT-LCP/croissant-maker/commit/1a34e1a123a5e8f0478f3e381ec2dbe97c951529))


### Documentation

* add --count-csv-rows to README ([725c6d3](https://github.com/MIT-LCP/croissant-maker/commit/725c6d3ea7368de6d12330d3d7cf48f177721145))
* add comprehensive technical overview of the project architecture, components, and handler system. ([8365bc4](https://github.com/MIT-LCP/croissant-maker/commit/8365bc4109920aa381a0af5de8eb14d32f09e751))
* add comprehensive technical overview of the project architecture, components, and handler system. ([3d8f87b](https://github.com/MIT-LCP/croissant-maker/commit/3d8f87b564456a49d5c4bfcc5e2c8502f597bce3))
* add PR report for modern Python tooling ([bc5db4b](https://github.com/MIT-LCP/croissant-maker/commit/bc5db4bbf308e2152648b1f86fb4f8860f78138f))
* document release-please workflow in README ([49bee84](https://github.com/MIT-LCP/croissant-maker/commit/49bee84c87152ad36feb31bf106434b8585c2720))
* update README for uv-based developer workflow ([65731f5](https://github.com/MIT-LCP/croissant-maker/commit/65731f5a611a69cab53e7e98057bbb8c8574f107))


### Build System

* **deps:** bump actions/checkout from 4 to 6 ([b71db40](https://github.com/MIT-LCP/croissant-maker/commit/b71db40b12b287c1ba81c72eeddeb842ff1326fb))
* **deps:** bump actions/checkout from 4 to 6 ([804f9aa](https://github.com/MIT-LCP/croissant-maker/commit/804f9aaebbfacf585525bb260a9f1dfbddefdddd))
* **deps:** bump astral-sh/setup-uv from 5 to 7 ([3427a4a](https://github.com/MIT-LCP/croissant-maker/commit/3427a4a2827649d9d7290555cb71f29d3284114a))
* **deps:** bump astral-sh/setup-uv from 5 to 7 ([a819966](https://github.com/MIT-LCP/croissant-maker/commit/a819966a68b2f9a649b3403f93809f13b5f3bf60))
* migrate to hatchling + uv with PEP 735 dependency groups ([ac1076d](https://github.com/MIT-LCP/croissant-maker/commit/ac1076d3f8ab2d7815aee3a06fc44176da902b69))
