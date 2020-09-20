# Kodi Recently Added Media for Home Assistant

Home Assistant component to feed [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card) with
Kodi's recently added media.

![Kodi Recently Added Media](https://raw.githubusercontent.com/boralyl/kodi-recently-added/master/assets/example.png)

**NOTE: This component only will work with Home Assistant version 0.115 and above. Additionally Kodi must be setup via the UI in the integrations section of the Home Assistant configuration.**

## HACS Installation

1. Search for `Kodi Recently Added Component` in the HACS Store tab.
2. Install the card: [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card)
3. Add the code to your `configuration.yaml` using the config options below.
4. Add the code for the card to your `ui-lovelace.yaml`, or via the lovelace dashboard.
5. **You will need to restart after installation for the component to start working.**

### Platform Configuration:

| key  | default | required | description                  |
| ---- | ------- | -------- | ---------------------------- |
| host |         | yes      | The host Kodi is running on. |

The host is the same host you entered when configuring Kodi via the integrations page.

### Sample configuration.yaml:

```yaml
sensor:
  - platform: kodi_recently_added
    host: 10.1.1.2

  - platform: kodi_recently_added
    host: 10.1.1.3
```

### Sample for ui-lovelace.yaml:

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

_NOTE: Currently genres, rating, and studio only work for Movies._
