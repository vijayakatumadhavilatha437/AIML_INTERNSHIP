import matplotlib.pyplot as plt

# Data
subjects = ['Python', 'Java', 'C', 'C++']
marks = [85, 70, 60, 75]

# Create bar chart
plt.bar(subjects, marks)

# Title and labels
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Show chart
plt.show()