### Making a heatmap of data sorted by state

In this example I am using wheat acreage harvested between 1911 and 2025 that Ellie downloaded from USDA NASS \
Note that I got a lot of help from the google default AI for this.

`````
#install packages as needed
library('usmap')
library('ggplot2')
library('dplyr')
library('data.table')
library('gganimate')
library('gifski')
library('plotly')
library('htmlwidgets')

#set your working directory
setwd("/Users/read0094/Desktop/Wheat")

#import the data and rename the columns
wheat_data=fread("Wheat_Acres_Harvested_By_State.txt")
wheat_data = wheat_data %>% rename(year=Year, state=State, acres=`Acres Harvested`)

#I did a quick test with just one year
#test=filter(wheat_data, Year==2000)
#test = test %>% rename(year=Year, state=State, acres=`Acres Harvested`)


#####To make a gif #####
#I ended up not liking this as much as the other plotly version

animatedmap=plot_usmap(data = wheat_data, values = "acres", color = "white") +
  scale_fill_continuous(
    name = "Harvested Acres", 
    labels = scales::comma,
    low = "#e5f5f0",   # Light green
    high = "#006d2c",  # Dark green
    guide = guide_colorbar(barwidth = 15, barheight = 2.0, title.position = "right")
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    text = element_text(size = 14),
    plot.title = element_text(face = "bold", size = 16)
  ) +
  # This dynamic label updates the title automatically for each year
  labs(
    title = "U.S. Harvested Acres in Year: {current_frame}",
    subtitle = "Data pulled from historical records"
  ) +
  # Tells gganimate to split the maps by the 'year' column
  transition_manual(year)


# Render and save the map as a GIF in your working directory
# Note that this saves a stack of images that can be visualized as a gif
animate(animatedmap, renderer = gifski_renderer("harvested_acres_history.gif"), width = 800, height = 600)
#####


###USING PLOTLY TO CREATE A SLIDER THING

#This package needs two letter state codes.  There's a cool little conversion but it requires no whitespaces in state names
wheat_data_clean <- wheat_data %>%
  mutate(
    # Strip accidental spaces from sides
    state_clean = trimws(as.character(state)),
    
    # Force standard Title Case (e.g., "texas" or "TEXAS" becomes "Texas")
    state_clean = stringr::str_to_title(state_clean),
    
    # Convert full names to abbreviations safely
    state_code = state.abb[match(state_clean, state.name)]
  )

# Calculate global scale boundaries
# I'm doing this so the heatmap scale is the same across years
min_acres <- min(wheat_data$acres, na.rm = TRUE)
max_acres <- max(wheat_data$acres, na.rm = TRUE)

# Make the interactive map
interactive_map <- plot_geo(wheat_data_clean, locationmode = 'USA-states') %>%
  add_trace(
    z = ~acres, 
    locations = ~state_code, 
    color = ~acres, 
    colors = 'Greens',
    frame = ~year, 
    zmin = min_acres,
    zmax = max_acres
  ) %>%
  layout(
    title = list(
      text = '<b>U.S. Wheat Harvested Acres by Year</b>',
      font = list(size = 22)
    ),
    geo = list(
      scope = 'usa', 
      projection = list(type = 'albers usa')
    )
  ) %>%
  
  # ONLY TECHNIQUE 2: Scaled up font sizes on the playback slider itself
  animation_slider(
    currentvalue = list(
      prefix = "YEAR: ", 
      font = list(
        size = 22,       # Makes the text directly above the slider track quite large
        color = "#d95f02", # Uses a distinct contrasting color to make it pop
        weight = "bold"
      )
    ),
    font = list(
      size = 14,         # Increases the size of individual timeline numbers under the track
      color = "#333333"
    )
  )

# Display the map locally
interactive_map

# save the map to the working directory
saveWidget(interactive_map, file = "harvested_acres_slider_fixed.html", selfcontained = TRUE)
`````
