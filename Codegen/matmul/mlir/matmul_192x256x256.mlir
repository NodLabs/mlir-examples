func @matmul(%a: memref<192x256xf32>, %b: memref<256x256xf32>, %c: memref<192x256xf32>) {
  linalg.matmul ins(%a, %b : memref<192x256xf32>, memref<256x256xf32>)
    outs(%c: memref<192x256xf32>)
  return
}