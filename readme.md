# Geo-Tour Content Modules

**Overview**
This repository is a library of **Content Modules** designed for use with the
[`maplibre-tour-control`](LINK_TO_PLUGIN_REPO) plugin.

The Tour Control plugin adds an interactive, cinematic storytelling engine to MapLibre-based
applications. This repository provides the "screenplays" (data) that the engine reads.
Acting as a "screenplay," the Content Modules choreograph the camera to automatically fly to
specific locations, tilt to 3D angles, and selectively highlight  features, while
the HTML files provide the commentary for each stop.

**Repository Structure**
Each subdirectory in this repository (e.g., `/USWest/`) is a self-contained **Content Module**.
A module consists of:
1.  **`manifest.json`**: The configuration file that choreographs camera movements,
    layer effects, and timing.
2.  **HTML Content**: A collection of slides/pages that provide the narrative text and media.

**Technical Requirements:**
    This is a **data-only repository**. To view a tour, you need a
    host application that meets the following criteria:
1.  **Map Engine:** Must use MapLibre GL JS .
2.  **Controller:** The `maplibre-tour-control` plugin, which manages the complete storytelling experience. It generates the tour
    user interface, animates the map camera, and renders the synchronized HTML narrative content.
3.  **Base Map:** Any standard MapLibre style (e.g., Satellite or Terrain).
    *   *Note on Effects:* The manifest references specific layer IDs to create visual
        highlighting effects. These layers are **optional**; if
        they are missing from the base map, the tour navigation and narrative will still
        function perfectly, but the specific feature highlight effects will not appear.
    
**Usage:**
  See `maplibre-tour-control`