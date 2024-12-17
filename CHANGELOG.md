# Changelog

## 0.1.0-alpha.6 (2024-12-17)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/niklub/label-studio-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#30](https://github.com/niklub/label-studio-python/issues/30)) ([7f7f2d1](https://github.com/niklub/label-studio-python/commit/7f7f2d10b9df25fb9f1a50369a3a14af911f721c))


### Chores

* **internal:** add support for TypeAliasType ([#36](https://github.com/niklub/label-studio-python/issues/36)) ([41fbd9a](https://github.com/niklub/label-studio-python/commit/41fbd9a45790b953b7cb3106f46661e4c8746772))
* **internal:** bump pydantic dependency ([#33](https://github.com/niklub/label-studio-python/issues/33)) ([f38e215](https://github.com/niklub/label-studio-python/commit/f38e21531536f98d8de2f9ce56262c8afd54eba1))
* **internal:** bump pyright ([#31](https://github.com/niklub/label-studio-python/issues/31)) ([ab9253b](https://github.com/niklub/label-studio-python/commit/ab9253b824fb4ad1cdb873d50c5120a6e8aa321a))
* **internal:** bump pyright ([#35](https://github.com/niklub/label-studio-python/issues/35)) ([4867930](https://github.com/niklub/label-studio-python/commit/4867930b4bab8082d523fe160a0f6d3c29519496))
* **internal:** codegen related update ([#37](https://github.com/niklub/label-studio-python/issues/37)) ([7b4d237](https://github.com/niklub/label-studio-python/commit/7b4d23769c14a1a2c3f0072a8fc16ebc14fefb2e))
* **internal:** codegen related update ([#38](https://github.com/niklub/label-studio-python/issues/38)) ([ddc21a7](https://github.com/niklub/label-studio-python/commit/ddc21a7e122f9d0e8ca8c70ca5b35d8c913bf294))
* **internal:** codegen related update ([#41](https://github.com/niklub/label-studio-python/issues/41)) ([ebb211f](https://github.com/niklub/label-studio-python/commit/ebb211fbb707329d068eb162916b75820c87447a))
* **internal:** codegen related update ([#42](https://github.com/niklub/label-studio-python/issues/42)) ([daaadd0](https://github.com/niklub/label-studio-python/commit/daaadd095a4eba9e93c396c2a525c5dc0dffeb91))
* **internal:** exclude mypy from running on tests ([#29](https://github.com/niklub/label-studio-python/issues/29)) ([e030b0e](https://github.com/niklub/label-studio-python/commit/e030b0e608b937d9baf317b08c4c193743eb2318))
* **internal:** fix compat model_dump method when warnings are passed ([#26](https://github.com/niklub/label-studio-python/issues/26)) ([8852b30](https://github.com/niklub/label-studio-python/commit/8852b309dd9a3ac2e34da48c397e0ad46cfb1f47))
* **internal:** remove some duplicated imports ([#39](https://github.com/niklub/label-studio-python/issues/39)) ([1b25947](https://github.com/niklub/label-studio-python/commit/1b25947b92a718fade19fb320dd3e3234276a9c6))
* **internal:** updated imports ([#40](https://github.com/niklub/label-studio-python/issues/40)) ([1c0a40b](https://github.com/niklub/label-studio-python/commit/1c0a40b46d08d1a4bd332888028ed86a66711d0e))
* make the `Omit` type public ([#32](https://github.com/niklub/label-studio-python/issues/32)) ([dae5000](https://github.com/niklub/label-studio-python/commit/dae5000c1d1a36562f38382487dfe2b52ff533e6))
* rebuild project due to codegen change ([#21](https://github.com/niklub/label-studio-python/issues/21)) ([286b792](https://github.com/niklub/label-studio-python/commit/286b79210f251eab1711814c59fdebe3fc79bfae))
* rebuild project due to codegen change ([#23](https://github.com/niklub/label-studio-python/issues/23)) ([d361c08](https://github.com/niklub/label-studio-python/commit/d361c0838f3ea27587b6f6f7b905510c9926af42))
* rebuild project due to codegen change ([#24](https://github.com/niklub/label-studio-python/issues/24)) ([cd7dcbc](https://github.com/niklub/label-studio-python/commit/cd7dcbced457126224ca3b5351efd78b2a582040))
* rebuild project due to codegen change ([#25](https://github.com/niklub/label-studio-python/issues/25)) ([51ed15a](https://github.com/niklub/label-studio-python/commit/51ed15a06d7cfdeb95c18b23a1a32f448a70dc7f))
* remove now unused `cached-property` dep ([#28](https://github.com/niklub/label-studio-python/issues/28)) ([9827974](https://github.com/niklub/label-studio-python/commit/98279742dff5d21b78d31563ebc5283361f4adb9))


### Documentation

* add info log level to readme ([#27](https://github.com/niklub/label-studio-python/issues/27)) ([4646aa2](https://github.com/niklub/label-studio-python/commit/4646aa2c5e925b593e6d21f49565fdf07b43319b))
* **readme:** example snippet for client context manager ([#43](https://github.com/niklub/label-studio-python/issues/43)) ([37d88a7](https://github.com/niklub/label-studio-python/commit/37d88a7c6b6057e302ca280d6eaa4a8a45e50aec))
* **readme:** fix http client proxies example ([#34](https://github.com/niklub/label-studio-python/issues/34)) ([9ad1710](https://github.com/niklub/label-studio-python/commit/9ad1710dac37474e4cec82f0dbe3ffc296ac4483))

## 0.1.0-alpha.5 (2024-05-20)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/niklub/label-studio-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([#18](https://github.com/niklub/label-studio-python/issues/18)) ([61a316a](https://github.com/niklub/label-studio-python/commit/61a316aab06e82bb69e9f2ec5e6bb7f9ff94c65a))

## 0.1.0-alpha.4 (2024-05-20)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/niklub/label-studio-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#15](https://github.com/niklub/label-studio-python/issues/15)) ([cdcba12](https://github.com/niklub/label-studio-python/commit/cdcba1290bd67c99ac7a5f166d96e14774244db9))

## 0.1.0-alpha.3 (2024-05-20)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/niklub/label-studio-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#12](https://github.com/niklub/label-studio-python/issues/12)) ([211d490](https://github.com/niklub/label-studio-python/commit/211d4908a9f4e4fc0d138f9d64eab33ddabfee85))

## 0.1.0-alpha.2 (2024-05-16)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/niklub/label-studio-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#9](https://github.com/niklub/label-studio-python/issues/9)) ([ec09634](https://github.com/niklub/label-studio-python/commit/ec09634cea576283eb114ce5f2e2923a4e1c87da))

## 0.1.0-alpha.1 (2024-05-16)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/niklub/label-studio-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#6](https://github.com/niklub/label-studio-python/issues/6)) ([72bd0f0](https://github.com/niklub/label-studio-python/commit/72bd0f0cbd20d6a26bdf2744c02ccb50b6272186))

## 0.0.1-alpha.1 (2024-05-16)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/niklub/label-studio-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* configure new SDK language ([c280c43](https://github.com/niklub/label-studio-python/commit/c280c43acb265520f7b0d38fed35899b29540774))
* go live ([#3](https://github.com/niklub/label-studio-python/issues/3)) ([fca8ad2](https://github.com/niklub/label-studio-python/commit/fca8ad2e3b1e2be9534079de2b6476fa96b83074))
