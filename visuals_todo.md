# Visuals To Create for GPU Presentation

## Required Images

### 1. **nvidia_stock_chart.png** (Slide 1 - Opening)
- **Description:** NVIDIA stock price chart showing dramatic rise to becoming the most valuable company
- **Type:** Stock chart/graph with dramatic upward trajectory
- **Suggested tool:** 
  - Screenshot from Google Finance/Yahoo Finance/TradingView showing NVDA stock 5-year or 10-year chart
  - Or use actual financial charting tools
  - Add annotation: "Most Valuable Company in the World"
- **Dimensions:** ~1800x1000px (landscape, full slide)
- **Note:** This is your conversation starter - make it visually striking!
- **Data point to highlight:** NVIDIA's market cap surpassing $3 trillion in 2024

### 2. **mumbai_map_placeholder.png** (Slide 3)
- **Description:** Map of Mumbai with location markers showing different areas and Andheri
- **Type:** Simple map illustration
- **Suggested tool:** Google Maps screenshot + annotations, or create in Figma/Canva
- **Dimensions:** ~1400x800px

### 3. **features_visual_placeholder.png** (Slide 4)
- **Description:** Visual icons representing travel features (distance icon, clock, rain cloud, calendar, traffic sign, construction)
- **Type:** Icon grid or infographic
- **Suggested tool:** Canva, Figma, or use icon sets (Font Awesome, Material Icons)
- **Dimensions:** ~800x1000px (portrait)

### 4. **matrix_mult_visual_placeholder.png** (Slide 8)
- **Description:** Visual representation of matrix multiplication showing dimensions
  - Two matrices being multiplied with dimensions labeled (e.g., [1000 x 50] × [50 x 10])
  - Show how rows × columns works
  - Color-code elements that multiply together
- **Type:** Educational diagram
- **Suggested tool:** PowerPoint/Keynote, or Python matplotlib, or manim for animation
- **Dimensions:** ~1600x700px
- **Note:** This is crucial for understanding!

### 5. **cpu_architecture_placeholder.png** (Slide 10)
- **Description:** Simplified diagram of CPU architecture
  - Show 8-16 cores
  - Each core labeled as "powerful"
  - Sequential flow arrows
- **Type:** Simplified architecture diagram
- **Suggested tool:** Draw.io, Lucidchart, or Figma
- **Dimensions:** ~800x1000px
- **Reference:** Look at simplified CPU block diagrams

### 6. **cpu_sequential_placeholder.png** (Slide 11)
- **Description:** Visualization of CPU doing matrix multiplication sequentially
  - Show matrix elements being processed one by one or in small batches
  - Use animation frames or numbered sequence
  - Visual timeline showing sequential nature
- **Type:** Diagram/flowchart
- **Suggested tool:** PowerPoint animation frames exported as PNG, or create with Python/matplotlib
- **Dimensions:** ~1400x800px

### 7. **gpu_architecture_placeholder.png** (Slide 12)
- **Description:** Simplified diagram of GPU architecture
  - Show grid of many small cores (could represent as small squares/circles)
  - Label showing "10,000+ cores"
  - Parallel structure obvious from layout
- **Type:** Simplified architecture diagram
- **Suggested tool:** Draw.io, Figma, or code-based (matplotlib grid)
- **Dimensions:** ~800x1000px
- **Reference:** NVIDIA CUDA architecture diagrams (simplified)

### 8. **gpu_parallel_placeholder.png** (Slide 13)
- **Description:** Visualization of GPU doing matrix multiplication in parallel
  - Show many matrix elements being computed simultaneously
  - Use color/highlighting to show parallel operations
  - Could be same matrix as #5 but with all elements highlighted at once
- **Type:** Diagram showing parallelism
- **Suggested tool:** PowerPoint, Python matplotlib, or animation tool
- **Dimensions:** ~1400x800px

### 9. **numpy_cupy_comparison_placeholder.png** (Slide 17)
- **Description:** Bar chart comparing timing
  - X-axis: NumPy (CPU) vs CuPy (GPU)
  - Y-axis: Time in seconds
  - Show dramatic difference (e.g., 45s vs 0.5s)
  - Add labels with exact numbers
- **Type:** Bar chart
- **Suggested tool:** Python (matplotlib/seaborn), or online chart maker
- **Dimensions:** ~1400x800px
- **Note:** Run actual benchmarks and use real numbers!

### 10. **pytorch_comparison_placeholder.png** (Slide 19)
- **Description:** Bar chart comparing PyTorch CPU vs GPU timing
  - Similar to #8 but for PyTorch
  - Show even more dramatic difference
  - Add labels with exact numbers
- **Type:** Bar chart
- **Suggested tool:** Python (matplotlib/seaborn), or online chart maker
- **Dimensions:** ~1400x800px
- **Note:** Run actual benchmarks and use real numbers!

---

## Priority Order

**Critical Priority (Must Have):**
1. nvidia_stock_chart.png (#1) - **CONVERSATION STARTER** - This sets up the entire talk!

**High Priority (Essential):**
2. matrix_mult_visual_placeholder.png (#4) - Core concept
3. numpy_cupy_comparison_placeholder.png (#9) - Proof of speedup
4. pytorch_comparison_placeholder.png (#10) - Proof of speedup
5. cpu_architecture_placeholder.png (#5) - CPU explanation
6. gpu_architecture_placeholder.png (#7) - GPU explanation

**Medium Priority (Very Helpful):**
7. cpu_sequential_placeholder.png (#6) - Shows CPU limitation
8. gpu_parallel_placeholder.png (#8) - Shows GPU advantage
9. mumbai_map_placeholder.png (#2) - Makes intro relatable

**Lower Priority (Nice to Have):**
10. features_visual_placeholder.png (#3) - Can work without it, just list

---

## Quick Tips

- All images should go in an `images/` folder in the same directory as the .tex file
- Keep consistent color scheme (recommend: dark blue for CPU, green for GPU, accent orange)
- For code-generated plots, use seaborn or matplotlib with 'ggplot' style
- For diagrams, stick to simple, clean designs (avoid too many colors/decorations)
- Test visibility: will they be readable from back of room?

---

## Alternative: Quick Workaround

If you need to present soon, you can:
1. Generate charts (#8, #9) using Python scripts (5 minutes each)
2. Use NVIDIA's official architecture diagrams for #4 and #6 (with attribution)
3. Create #3 in Google Slides or PowerPoint (15 minutes)
4. Skip #2, #5, #7 for first version (slides work without them)

