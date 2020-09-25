**Install Deps**
See here to install deps via ./install_deps.sh
https://github.com/NodLabs/mlir-examples

### How to run:
**Conv2d Example**
```
cd tf_conv2d

path/to/tensorflow/bazel-bin/tensorflow/compiler/mlir/tf-mlir-translate --savedmodel-objectgraph-to-mlir ./tf_conv2d/tf_saved_model > translated_conv.mlir

path/to/tensorflow/bazel-bin/tensorflow/compiler/mlir/tf-opt --symbol-dce --tf-executor-graph-pruning --tf-guarantee-all-funcs-one-use --tf-standard-pipeline --tf-device-index-selector --inline --canonicalize --tf-device-decompose-resource-ops --tf-shape-inference --tf-functional-control-flow-to-cfg --inline --symbol-dce --canonicalize --tf-saved-model-optimize-global-tensors --tf-saved-model-freeze-global-tensors --xla-legalize-tf --canonicalize --tf-saved-model-optimize-global-tensors ./translated_conv.mlir
```

tf-opt when the `tf-saved-model-optimize-global-tensors` flag is first encountered with the following error:
 ```
 error: is not immutable, try running tf-saved-model-optimize-global-tensors to prove tensors are immutable
  "tf_saved_model.global_tensor"() {is_mutable, sym_name = "__sm_node5__m.conv2d.kernel", tf_saved_model.exported_names = ["m.conv2d.kernel", "m.conv2d.variables.0", "m.conv2d.keras_api.variables.0", "m.conv2d.trainable_variables.0", "m.conv2d.keras_api.trainable_variables.0"], type = tensor<3x3x1x32xf32>, value = dense<"0x8CD6. 
```

### How to run:
**MNIST Example**
```
path/to/tensorflow/bazel-bin/tensorflow/compiler/mlir/tf-mlir-translate --savedmodel-objectgraph-to-mlir ./tf_mnist/tf_saved_model > translated_mnist.mlir
```

The translation does not even happen and the following output is obtained:
```
2020-09-24 18:27:21.207388: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library libcudart.so.11.0
2020-09-24 18:27:21.260534: I tensorflow/cc/saved_model/bundle_v2.cc:32] Reading SavedModel from: ./tf_mnist/tf_saved_model
2020-09-24 18:27:21.261778: I tensorflow/cc/saved_model/bundle_v2.cc:55] Reading SavedModel debug info (if present) from: ./tf_mnist/tf_saved_model
2020-09-24 18:27:21.300066: E tensorflow/compiler/mlir/tensorflow/translate/tf_mlir_translate.cc:163] SavedModel import failed: Invalid argument: Exported function with exported name(s) 'm.flatten.__call__', 'm.flatten.keras_api.__call__' with multiple concrete functions. Add @tf.function(input_signature=[...]) on this function, or use a narrower list of exported names that excludes this function.
```