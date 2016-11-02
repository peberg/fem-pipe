
# find source
threshold1 = FindSource('Threshold1')

# set active source
SetActiveSource(threshold1)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [660, 497]

# get display properties
threshold1Display = GetDisplayProperties(threshold1, view=renderView1)

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', 'valuesC'))

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'valuesC'
valuesCLUT = GetColorTransferFunction('valuesC')
valuesCLUT.RGBPoints = [-0.010476155927503138, 0.231373, 0.298039, 0.752941, 0.012684562177662569, 0.865003, 0.865003, 0.865003, 0.035845280282828275, 0.705882, 0.0156863, 0.14902]
valuesCLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'valuesC'
valuesCPWF = GetOpacityTransferFunction('valuesC')
valuesCPWF.Points = [-0.010476155927503138, 0.0, 0.5, 0.0, 0.035845280282828275, 1.0, 0.5, 0.0]
valuesCPWF.ScalarRangeInitialized = 1

# change representation type
threshold1Display.SetRepresentationType('Surface')

# find source
threshold2 = FindSource('Threshold2')

# set active source
SetActiveSource(threshold2)

# get color transfer function/color map for 'Marker'
markerLUT = GetColorTransferFunction('Marker')
markerLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
markerLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Marker'
markerPWF = GetOpacityTransferFunction('Marker')
markerPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
markerPWF.ScalarRangeInitialized = 1

# find source
clip1 = FindSource('Clip1')

# set active source
SetActiveSource(clip1)

# get display properties
clip1Display = GetDisplayProperties(clip1, view=renderView1)

# change representation type
clip1Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'valuesC'))

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
valuesCLUT.RescaleTransferFunction(-0.000003, 0.000003)

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 252

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 126

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 107

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 98

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 88

# Properties modified on valuesCLUT
valuesCLUT.NumberOfTableValues = 24

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1)

###########################


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [660, 497]

# get color legend/bar for valuesCLUT in view renderView1
valuesCLUTColorBar = GetScalarBar(valuesCLUT, renderView1)
valuesCLUTColorBar.ComponentTitle = ''

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
valuesCLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.AutomaticLabelFormat = 0

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.Title = 'E (V)'

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.LabelFormat = '%-#6.1g'

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.NumberOfLabels = 3

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.AutomaticAnnotations = 0
valuesCLUTColorBar.AspectRatio = 15.0

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.TitleFontFamily = 'Times'
valuesCLUTColorBar.LabelFontFamily = 'Times'

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.TitleBold = 1
valuesCLUTColorBar.TitleFontSize = 12

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.TitleFontSize = 10
valuesCLUTColorBar.LabelFontSize = 9

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.LabelFormat = '%-#2.1e'

# Properties modified on valuesCLUTColorBar
valuesCLUTColorBar.RangeLabelFormat = '%4.1e'


# save screenshot
SaveScreenshot('figs/3d_output_field.png', magnification=1, quality=100, view=renderView1)