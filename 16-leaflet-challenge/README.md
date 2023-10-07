# <span style="color:tan"> Unit 16 Leaflet Challenge </span>

## <span style="color:red"> **Background**  </span>

The United States Geological Survey, or USGS for short, is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes.

The USGS is interested in building a new set of tools that will allow them to visualize their earthquake data. They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it. In this challenge, you have been tasked with developing a way to visualize USGS data that will allow them to better educate the public and other government organizations (and hopefully secure more funding) on issues facing our planet.

##  <span style="color:orange"> **Before You Begin** </span>

1. Create a new repository for this project called leaflet-challenge. Do not add this Challenge to an existing repository.
2. Clone the new repository to your computer.
3. Inside your local git repository, create a directory for the Leaflet challenge. Use the folder names to correspond to the challenges: Leaflet-Part-1 and Leaflet-Part-2.
4. This Challenge uses both HTML and JavaScript, so be sure to add all the necessary files. These will be the main files to run for analysis.
5. Push the above changes to GitHub.

##  <span style="color:green">  **Instructions** </span>
The instructions for this activity are broken into two parts:
* Part 1: Create the Earthquake Visualization
* Part 2: Gather and Plot More Data (Optional with no extra points earning)

###  <span style="color:tan">  **Part 1: Create the Earthquake Visualization** </span>

![Alt text](https://static.bc-edx.com/data/dl-1-1/m15/lms/img/2-BasicMap.jpg "Earthquake Map")

Your first task is to visualize an earthquake dataset. Complete the following steps:
1. Get your dataset. To do so, follow these steps:
    * The USGS provides earthquake data in a number of different formats, updated every 5 minutes. Visit the  <a href = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php" target = "_blank"> USGS GeoJSON Feed </a> page and choose a dataset to visualize. The following image is an example screenshot of what appears when you visit this link:
    
    ![Alt text](https://static.bc-edx.com/data/dl-1-1/m15/lms/img/3-Data.jpg "USGS GeoJSON Feed main page")

    * When you click a dataset (such as "All Earthquakes from the Past 7 Days"), you will be given a JSON representation of that data. Use the URL of this JSON to pull in the data for the visualization. The following image is a sampling of earthquake data in JSON format:

     ![Alt text](https://static.bc-edx.com/data/dl-1-1/m15/lms/img/4-JSON.jpg "USGS GeoJSON data")
     
2. Import and visualize the data by doing the following:
    * Using Leaflet, create a map that plots all the earthquakes from your dataset based on their longitude and latitude.
        * Your data markers should reflect the magnitude of the earthquake by their size and the depth of the earthquake by color. Earthquakes with higher magnitudes should appear larger, and earthquakes with greater depth should appear darker in color.
        * Hint: The depth of the earth can be found as the third coordinate for each earthquake.

    * Include popups that provide additional information about the earthquake when its associated marker is clicked.
    * Create a legend that will provide context for your map data.
    * Your visualization should look something like the preceding map.

###  <span style="color:tan">  **Part 2: Gather and Plot More Data (Optional with no extra points earning)** </span>
Plot a second dataset on your map to illustrate the relationship between tectonic plates and seismic activity. You will need to pull in this dataset and visualize it alongside your original data. Data on tectonic plates can be found at <a href = "https://github.com/fraxen/tectonicplates" target = "_blank"> https://github.com/fraxen/tectonicplates </a> 

This part is completely optional; you can complete this part as a way to challenge yourself and boost your new skills.

The following image is an example screenshot of what you should produce:

![Alt text](https://static.bc-edx.com/data/dl-1-1/m15/lms/img/5-Advanced.jpg "Earthquake and Tectonic plate map")


Perform the following tasks:
* Plot the tectonic plates dataset on the map in addition to the earthquakes.
* Add other base maps to choose from.
* Put each dataset into separate overlays that can be turned on and off independently.
* Add layer controls to your map.

- - -

© 2023 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.