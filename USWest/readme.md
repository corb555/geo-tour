
# Western US Geology Tour (Content Module)

**Overview:**
This repository contains the **narrative content and configuration** for an interactive,
cinematic map tour designed for the `maplibre-tour-control` plugin. Acting as a
"screenplay," the included manifest choreographs the camera to automatically fly to
specific locations, tilt to 3D angles, and selectively highlight geologic features, while
the HTML files provide the commentary for each stop.

**Content:**
The "Western US Geology Tour" provides a dramatic visual exploration of the tectonic and
geomorphic forces that have sculpted the American West. The journey covers a dozen high-level topics
and locations. It begins on the coast with the violent plate interactions of the San
Andreas and Cascadia faults, before moving inland to trace the history of explosive
volcanism along the Ring of Fire and the Yellowstone Hotspot track. The tour also
examines the  impact of water and ice—from the glacial carving of Puget Sound to
the cataclysmic Missoula Floods—and concludes with the deep crustal stretching that
created the Basin and Range, the Grand Canyon, and the Rio Grande Rift.

**Target Audience & Duration:**
This tour is designed for **general audiences and students 12 or older** with an interest in earth
science, requiring no prior geological training to understand. It takes approximately
**10-15 minutes** to complete at a leisurely reading pace.

**Technical Requirements:**
This is a **data-only repository**. To view this tour, these files must be loaded into a
host application that meets the following criteria:
1.  **Map Engine:** MapLibre GL JS .
2.  **Controller:** The `maplibre-tour-control` plugin, which manages the complete storytelling experience. It generates the tour 
user interface, animates the map camera, and renders the synchronized HTML narrative content.
3.  **Base Map:** Any standard MapLibre style (e.g., Satellite or Terrain).
    *   *Note on Effects:* This manifest references specific layer IDs to create visual
        highlighting effects. These layers are **optional**; if
        they are missing from the base map, the tour navigation and narrative will still
        function perfectly, but the specific feature highlight effects will not appear.