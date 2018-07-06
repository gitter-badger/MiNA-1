# @Dataset(label="Image to process:") dataset
# @String(label="Thresholding method: ", value="otsu", choices={"ij1", "li", "minimum", "otsu", "triangle"}) threshold_method
# @String(label="Skeletonizing routine: ", value="Morphological", choices={"GuoHall", "Hilditch", "Morphological", "ZhangSuen"}) thinning_method
# @String(label="Preprocessing: ", value="", style="text area") preprocessor
# @String(label="Preprocessing type: ", value="None", choices={"None", "Beanshell", "Groovy", "J1 Macro", "Javascript", "Jython"}) preprocessor_type
# @UIService ui
# @OpService ops

import sciencetoolkit.math
import sciencetoolkit.rendering

def run(dataset, threshold_method, thinning_method, preprocessor, preprocessor_type):

    # Generate binary and skeleton...
    binary = MiNA.processing.make_binary_copy(ops, dataset, threshold_method)
    ui.show("Binary", binary)

    skeleton = MiNA.processing.make_skeleton_copy(ops, binary, thinning_method)
    ui.show("Skeleton", skeleton)

    # Generate the graphic and ask the user if it is OK...
    #skel_result = MiNA.analysis.generate_skeleton_result(dataset, binary, skeleton)
    #MiNA.ui.render_overlay(dataset, binary, skel_result)
    #quality_check = MiNA.ui.quality_control_dialog()

    # Generate measurements and add to the results table...
    #bin_analysis = MiNA.analysis.connected_component_analysis(binary)
    #skel_analysis = MiNA.analysis.skeleton_analysis(skel_result)
    #MiNA.ui.update_results_table(bin_analysis, skel_analysis)

if __name__ == "__main__" or __name__=="__builtin__":
    run(dataset, threshold_method, thinning_method, preprocessor, preprocessor_type)
