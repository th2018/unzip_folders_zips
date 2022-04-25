import arcpy
import os
os.getcwd()
arcpy.env.workspace =r"C:\Users\taohuang\Downloads\mtbs_perimeter_data\west_mtbs_perimeter_data"
arcpy.SelectLayerByLocation_management("mtbs_perims_DD","INTERSECT","Western_states")
arcpy.FeatureClassToFeatureClass_conversion("mtbs_perims_DD",r"C:\Users\taohuang\Downloads\mtbs_perimeter_data","west_mtbs_perims_DD")

