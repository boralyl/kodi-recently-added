# Kodi Recently Added Media for Home Assistant

[![](https://img.shields.io/github/release/boralyl/kodi-recently-added/all.svg?style=for-the-badge)](https://github.com/boralyl/kodi-recently-added/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![](https://img.shields.io/github/license/boralyl/kodi-recently-added?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/workflow/status/boralyl/kodi-recently-added/Python%20package?style=for-the-badge)](https://github.com/boralyl/kodi-recently-added/actions)

Home Assistant component to feed [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card) with
Kodi's recently added media.

![Kodi Recently Added Media](https://raw.githubusercontent.com/boralyl/kodi-recently-added/master/assets/example.png)

# Table of Contents

- [Installation](#installation)
  - [Pre-Installation](#pre-installation)
  - [HACS Install](#hacs-install)
  - [Manual Install](#manual-install)
- [Configuration](#configuration)
  - [Configuring via YAML](#configuring-via-yaml)
  - [Configuring via Integrations](#configuring-via-integrations)
- [Upgrading from configuration.yaml to UI integration](#upgrading-from-configurationyaml-to-ui-integration)
- [Known Issues](#known-issues)

## Installation

### Pre-Installation

**NOTE: This component only works with Home Assistant version 0.115 and above. Additionally Kodi must be setup via the UI in the integrations section of the Home Assistant configuration.**

### HACS Install

1. Search for `Kodi Recently Added Component` under `Integrations` in the HACS Store tab.
2. Install the card: [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card)
3. ~~Add the code to your `configuration.yaml` using the config options below.~~ (This is deprecated and it's recommended to add the integration via the Home Assistant Integrations if you are using >= v2.0.0)
4. Add the code for the card to your `ui-lovelace.yaml`, or via the lovelace dashboard.
5. **You will need to restart after installation for the component to start working.**

### Manual Install

1. In your `/config` directory, create a `custom_components` folder if one does not exist.
2. Copy the [kodi_recently_added](https://github.com/boralyl/kodi-recently-added/tree/master/custom_components) folder and all of it's contents from to your `custom components` directory.
3. Restart Home Assistant.

## Configuration

### Configuring via YAML

| key          | required | default | description                                                                                                         |
| ------------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| host         | yes      | --      | The host Kodi is running on. This is the same host that was configured when adding the Kodi integration via the UI. |
| hide_watched | no       | false   | Indicates if watched media should be skipped or not.                                                                |

The host is the same host you entered when configuring Kodi via the integrations page.

#### Sample configuration.yaml:

```yaml
sensor:
  - platform: kodi_recently_added
    host: 10.1.1.2
    hide_watched: true

  - platform: kodi_recently_added
    host: 10.1.1.3
```

#### Sample for ui-lovelace.yaml:

```yaml
- type: custom:upcoming-media-card
  entity: sensor.kodi_recently_added_tv
  title: Recently Added Episodes
  image_style: fanart

- type: custom:upcoming-media-card
  entity: sensor.kodi_recently_added_movies
  title: Recently Added Movies
  image_style: fanart
```

### Configuring via Integrations

TODO

## Upgrading from configuration.yaml to UI Integration

TODO

## Known Issues

Below is a list of known issues that either can't be fixed by changes to the component
itself due to external factors.

### Artwork does not load when using the upcoming-media-card

One reason this could occur is if you setup you Home Assistance instance to use SSL and
your Kodi instance does not use SSL. When the upcoming-media-card tries to load the
artwork it will fail to do so since modern browsers do not allow loading insecure requests.
See [#6](https://github.com/boralyl/kodi-recently-added/issues/6) for more details and
possible workarounds.

### Genres, ratings and studios don't show up for TV Shows

Currently genres, rating, and studio are only populated for Movies. This is a limitation
of the data Kodi stores for TV shows.
