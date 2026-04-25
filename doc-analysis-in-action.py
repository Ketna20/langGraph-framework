# Example 1: Simple Calculations
messages = [HumanMessage(content="Divide 6790 by 5")]
messages = react_graph.invoke({"messages": messages, "input_file": None})

# Show the messages
for m in messages['messages']:
    m.pretty_print()

# The conversation would proceed:
# Human: Divide 6790 by 5

# AI Tool Call: divide(a=6790, b=5)

# Tool Response: 1358.0

# Alfred: The result of dividing 6790 by 5 is 1358.0.


# Example 2: Analyzing Master Wayne’s Training Documents
messages = [HumanMessage(content="According to the note provided by Mr. Wayne in the provided images. What's the list of items I should buy for the dinner menu?")]
messages = react_graph.invoke({"messages": messages, "input_file": "Batman_training_and_meals.png"})

# The interaction would proceed:
# Human: According to the note provided by Mr. Wayne in the provided images. What's the list of items I should buy for the dinner menu?

# AI Tool Call: extract_text(img_path="Batman_training_and_meals.png")

# Tool Response: [Extracted text with training schedule and menu details]

# Alfred: For the dinner menu, you should buy the following items:

# 1. Grass-fed local sirloin steak
# 2. Organic spinach
# 3. Piquillo peppers
# 4. Potatoes (for oven-baked golden herb potato)
# 5. Fish oil (2 grams)

# Ensure the steak is grass-fed and the spinach and peppers are organic for the best quality meal.
