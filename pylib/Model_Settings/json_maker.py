import json
import collections
import numpy as np
import os

def write_json_file(filename, datafile):
    filename = 'Model_Settings/'+filename
    datafile = collections.OrderedDict(sorted(datafile.items()))
    with open(filename, 'w') as outFile:
        json.dump(datafile, outFile, indent=0)

def _set_folders(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
# Twin Common Parameters
trainLogDirBase = '../Data/kitti/logs/tfdh_twin_py_logs/train_logs/'
testLogDirBase = '../Data/kitti/logs/tfdh_twin_py_logs/test_logs/'
warpedTrainDirBase = '../Data/kitti/train_tfrecords_iterative/'
warpedTestDirBase = '../Data/kitti/test_tfrecords_iterative/'
####################################################################################
# Data Parameters
numTrainDatasetExamples_desc = "Number of images to process in train dataset"
numTestDatasetExamples_desc = "Number of images to process in test dataset"
trainDataDir_desc = "Directory to read training samples"
testDataDir_desc = "Directory to read test samples"
warpedTrainDataDir_desc = "Directory where to write wrapped train images"
warpedTestDataDir_desc = "Directory where to write wrapped test images"
trainLogDir_desc = "Directory where to write train event logs and checkpoints"
testLogDir_desc = "Directory where to write test event logs and checkpoints"
tMatTrainDir_desc = "tMat Output folder for train"
tMatTestDir_desc = "tMat Output folder for test"
writeWarped_desc = "Flag showing if warped images should be written"
pretrainedModelCheckpointPath_desc = "If specified, restore this pretrained model before beginning any training"
# Image Parameters
imageDepthRows_desc = "Depth Image Height (ROWS)"
imageDepthCols_desc = "Depth Image Width (COLS)"
imageDepthChannels_desc = "Depth Image channels, number of stacked images"
# PCL Parameters
pclRows_desc = "3 rows, xyz of Point Cloud"
pclCols_desc = "Unified number of points (columns) in the Point Cloud"
# tMat Parameters
tMatRows_desc = "rows in transformation matrix"
tMatCols_desc = "cols in transformation matrix"
# Model Parameters
modelName_desc = "Name of the model file to be loaded from Model_Factory"
modelShape_desc = "Network model with 8 convolutional layers with 2 fully connected layers"
numParallelModules_desc = "Number of parallel modules of the network"
batchNorm_desc = "Should we use batch normalization"
weightNorm_desc = "Should we use weight normalization"
optimizer_desc = "Type of optimizer to be used [AdamOptimizer, MomentumOptimizer, GradientDescentOptimizer]"
initialLearningRate_desc = "Initial learning rate."
learningRateDecayFactor_desc = "Learning rate decay factor"
numEpochsPerDecay_desc = "Epochs after which learning rate decays"
momentum_desc = "Momentum Optimizer: momentum"
epsilon_desc = "epsilon value used in AdamOptimizer"
dropOutKeepRate_desc = "Keep rate for drop out"
clipNorm_desc = "Gradient global normalization clip value"
lossFunction_desc = "Indicates type of the loss function to be used [L2, CrossEntropy, ..]"
# Train Parameters
trainBatchSize_desc = "Batch size of input data for train"
testBatchSize_desc = "Batch size of input data for test"
outputSize_desc = "Final output size"
trainMaxSteps_desc = "Number of batches to run"
testMaxSteps_desc = "Number of batches to run during test. numTestDatasetExamples = testMaxSteps x testBatchSize" 
usefp16_desc = "Use 16 bit floating point precision"
logDevicePlacement_desc = "Whether to log device placement"

data = {
    # Data Parameters
    'numTrainDatasetExamples' : 20400,
    'numTestDatasetExamples' : 2790,
    'trainDataDir' : '../Data/kitti/train_tfrecords',
    'testDataDir' : '../Data/kitti/test_tfrecords',
    'warpedTrainDataDir' : warpedTrainDirBase+'',
    'warpedTestDataDir' : warpedTestDirBase+'',
    'trainLogDir' : trainLogDirBase+'',
    'testLogDir' : testLogDirBase+'',
    'tMatTrainDir' : trainLogDirBase+'/target',
    'tMatTestDir' : testLogDirBase+'/target',
    'writeWarped' : False,
    'pretrainedModelCheckpointPath' : '',
    # Image Parameters
    'imageDepthRows' : 128,
    'imageDepthCols' : 512,
    'imageDepthChannels' : 2, # All PCL files should have same cols
    # PCL Parameters
    'pclRows' : 3,
    'pclCols' : 62074,
    # tMat Parameters
    'tMatRows' : 3,
    'tMatCols' : 4,
    # Model Parameters
    'modelName' : '',
    'modelShape' : [64, 64, 64, 64, 128, 128, 128, 128, 1024],
    'numParallelModules' : 2,
    'batchNorm' : True,
    'weightNorm' : False,
    'optimizer' : 'MomentumOptimizer', # AdamOptimizer MomentumOptimizer GradientDescentOptimizer
    'initialLearningRate' : 0.005,
    'learningRateDecayFactor' : 0.1,
    'numEpochsPerDecay' : 10000.0,
    'momentum' : 0.9,
    'epsilon' : 0.1,
    'dropOutKeepRate' : 0.5,
    'clipNorm' : 1.0,
    'lossFunction' : 'L2',
    # Train Parameters
    'trainBatchSize' : 16,
    'testBatchSize' : 16,
    'outputSize' : 6, # 6 Params
    'trainMaxSteps' : 30000,
    'testMaxSteps' : 1,
    'usefp16' : False,
    'logDevicePlacement' : False
    }
data['testMaxSteps'] = int(np.ceil(data['numTestDatasetExamples']/data['testBatchSize']))
####################################################################################
####################################################################################
####################################################################################
####################################################################################
##############
reCompileJSON = True

def write_single():
    # Single Common Parameters
    trainLogDirBase = '../Data/kitti/logs/tfdh_py_logs/train_logs/'
    testLogDirBase = '../Data/kitti/logs/tfdh_py_logs/test_logs/'
    data['trainDataDir'] = '../Data/kitti/train_tfrecords'
    data['testDataDir'] = '../Data/kitti/test_tfrecords'

    data['modelName'] = 'cnn_8l2f'

    writeWarpedImages = False

    ##############
    if reCompileJSON:
        data['trainLogDir'] = trainLogDirBase+'170126_SIN_B'
        data['testLogDir'] = testLogDirBase+'170126_SIN_B'
        data['trainMaxSteps'] = 90000
        data['numEpochsPerDecay'] = 30000.0
        data['trainBatchSize'] = 64
        data['testBatchSize'] = 64
        data['testMaxSteps'] = int(np.ceil(data['numTestDatasetExamples']/data['testBatchSize']))
        data['modelShape'] = [64, 64, 64, 64, 128, 128, 128, 128, 1024]
        data['batchNorm'] = True
        data['weightNorm'] = False
        write_json_file('170126_SIN_B.json', data)

    if reCompileJSON:
        data['trainLogDir'] = trainLogDirBase+'170126_SIN_W'
        data['testLogDir'] = testLogDirBase+'170126_SIN_W'
        data['trainMaxSteps'] = 90000
        data['numEpochsPerDecay'] = 30000.0
        data['trainBatchSize'] = 20
        data['testBatchSize'] = 20
        data['testMaxSteps'] = int(np.ceil(data['numTestDatasetExamples']/data['testBatchSize']))
        data['modelShape'] = [64, 64, 64, 64, 128, 128, 128, 128, 1024]
        data['batchNorm'] = False
        data['weightNorm'] = True
        write_json_file('170126_SIN_W.json', data)

    if reCompileJSON:
        data['trainLogDir'] = trainLogDirBase+'170126_SIN_BW'
        data['testLogDir'] = testLogDirBase+'170126_SIN_BW'
        data['trainMaxSteps'] = 90000
        data['numEpochsPerDecay'] = 30000.0
        data['trainBatchSize'] = 20
        data['testBatchSize'] = 20
        data['testMaxSteps'] = int(np.ceil(data['numTestDatasetExamples']/data['testBatchSize']))
        data['modelShape'] = [64, 64, 64, 64, 128, 128, 128, 128, 1024]
        data['batchNorm'] = True
        data['weightNorm'] = True
        write_json_file('170126_SIN_BW.json', data)
    ##############

def recompile_json_files():
    write_single()
    print("JSON files updated")
