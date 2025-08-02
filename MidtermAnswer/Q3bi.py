i) 
import pandas as pd
# Given dictionary
data = {'Name': ['Ali', 'Sara', 'John'],
        'Score': [88, 92, 75]}
# Create DataFrame
df = pd.DataFrame(data)
# Add 'Pass' column based on Score
df['Pass'] = df['Score'].apply(lambda x: 'Yes' if x >= 80 else 'No')
# Display students who passed
passed_students = df[df['Pass'] == 'Yes']
print("Full DataFrame:\n", df)
print("\nStudents who passed:\n", passed_students)
