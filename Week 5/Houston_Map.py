
# coding: utf-8

# In[6]:


import arcgis
from  arcgis import GIS
# Create a GIS object, as an anonymous user for this example
gis = GIS()


# ## Texas Map

# In[7]:


# Create a map widget
map1 = gis.map('Texas') # Passing a place name to the constructor
                        # will initialize the extent of the map.
map1


# ### Changing the zoom

# In[13]:


map1.zoom = 10


# ### Houston Area

# In[11]:


map1.center = [29.7604, -95.3698]


# In[14]:


location = arcgis.geocoding.geocode('Houston Area, TX', max_locations=1)[0]
map1.extent = location['extent']


# ### Changing Basemaps

# In[15]:


map1.basemaps


# In[16]:


map1.basemap = 'dark-gray'

