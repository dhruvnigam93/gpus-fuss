Audience: Python beginners and intermediates with almost no background in machine learning at the MumPy conference. So can't assume any machine learning stuff.

Presentation intent:
I want to tell them why GPUs are so important. They must be wondering why everyone is talking about GPUs now suddenly, and they might also know that they are used in gaming, but what do AI and gaming have in common? By revealing the link to be matrix multiplication (matmul), I want to motivate the GPU architecture and also show them how in Python they can use GPUs for their own purposes.

---

Presentation outline:

1. **Intro to machine learning with a relatable example**
   - Let's say I wanted to predict how much time it will take to reach Andheri from any location where I live
   - What features would we consider? Distance, time of day, raining or not, weekday/weekend, traffic conditions, etc.
   - Traditional approach: write if-else rules based on experience
   - ML approach: convert all these factors into numbers and learn a function

2. **From simple prediction to matrix multiplication**
   - For one location: multiply each feature by a weight, add them up → predicted time
   - Example: (distance × w1) + (time_of_day × w2) + (is_raining × w3) + (is_weekend × w4) = predicted_time
   - But what if we have:
     - 50 features instead of 4?
     - Want to predict for 1000 locations at once?
     - Have multiple layers of transformations (deep learning)?
   - This becomes matrix multiplication: [features matrix] × [weights matrix] = [predictions]
   - demo at http://matrixmultiplication.xyz/
   - Show the scale: modern ML models do billions of these operations

3. **Why CPUs struggle with this**
   - CPU architecture: Few powerful cores (4-16 typically)
   - Designed for sequential tasks: do step 1, then step 2, then step 3
   - Great for general-purpose computing, but matrix multiplication is inherently parallel
   - Analogy: Like having 8 very smart people solving 10,000 simple math problems one by one

4. **Why GPUs excel at matrix multiplication**
   - GPU architecture: Thousands of smaller cores (e.g., 10,000+ CUDA cores)
   - Designed for parallel tasks: do all steps simultaneously
   - Each core can handle one multiplication independently
   - Analogy: Like having 10,000 people each solving one math problem at the same time
   - Originally designed for graphics (brief mention: 3D transformations and rendering also use matrix math)

5. **Seeing is believing: Python timing examples**
   - Demo 1: NumPy on CPU vs CuPy on GPU for large matrix multiplication
     - Show code side by side
     - Time the operations
     - Show 10-100x speedup
   
   - Demo 2: PyTorch CPU vs PyTorch GPU
     - Simple neural network forward pass
     - Show how to move tensors to GPU with `.to('cuda')`
     - Compare timing
     - Show even more dramatic speedup with larger matrices

6. **Practical takeaways for the audience**
   - When should you care about GPUs?
     - Large matrices (thousands of rows/columns)
     - Repeated operations (training loops)
     - Real-time requirements
   - How to get started:
     - Google Colab (free GPU access)
     - Cloud providers (AWS, GCP, Azure)
     - Local GPU if doing serious work
   - Tools in Python ecosystem: PyTorch, TensorFlow, CuPy, JAX

7. **Wrap-up**
   - Modern AI = lots of matrix multiplication
   - Matrix multiplication = embarrassingly parallel
   - GPUs = parallel processing powerhouses
   - That's why every AI breakthrough now mentions GPU hours!
