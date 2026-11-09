from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='L', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        if self.page_no() == 1:
            self.set_fill_color(102, 126, 234)
            self.rect(0, 0, 297, 30, 'F')
            self.set_xy(10, 5)
            self.set_font('Helvetica', 'B', 18)
            self.set_text_color(255, 255, 255)
            self.cell(0, 10, 'Data Scientist Learning Timetable', new_x='LMARGIN', new_y='NEXT', align='C')
            self.set_xy(10, 15)
            self.set_font('Helvetica', '', 11)
            self.cell(0, 6, '8-Week Intensive Plan  |  8 Hours/Day  |  9:00 AM - 5:00 PM', new_x='LMARGIN', new_y='NEXT', align='C')
            self.set_xy(10, 22)
            self.set_font('Helvetica', 'I', 9)
            self.cell(0, 5, 'Python  |  SQL  |  Pandas  |  NumPy  |  Machine Learning', new_x='LMARGIN', new_y='NEXT', align='C')
            self.set_y(35)
        else:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, 'Data Scientist Learning Timetable - 8 Weeks', new_x='LMARGIN', new_y='NEXT', align='R')
            self.set_y(15)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, f'Page {self.page_no()}/{{nb}}', align='C')

    def section_title(self, title, subtitle=''):
        self.set_fill_color(45, 52, 54)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, f'  {title}', new_x='LMARGIN', new_y='NEXT', fill=True)
        if subtitle:
            self.set_x(10)
            self.set_font('Helvetica', 'I', 8)
            self.cell(0, 5, f'  {subtitle}', new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

    def phase_box(self, phase, weeks, focus, color):
        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 9)
        x = self.get_x()
        y = self.get_y()
        self.cell(65, 18, '', fill=True, new_x='END')
        self.set_xy(x + 2, y + 2)
        self.set_font('Helvetica', 'B', 9)
        self.cell(61, 6, phase, align='C')
        self.set_xy(x + 2, y + 9)
        self.set_font('Helvetica', '', 7)
        self.multi_cell(61, 4, f'{weeks}\n{focus}', align='C')
        self.set_xy(x + 67, y)

    def day_row(self, time, topic, activity, resource=''):
        self.set_text_color(0, 0, 0)
        col_widths = [28, 55, 130, 55]
        x_start = self.get_x()

        # Check if we need a new page
        if self.get_y() > 180:
            self.add_page()

        y_before = self.get_y()

        # Time column
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(108, 92, 231)
        self.set_fill_color(240, 240, 255)
        self.multi_cell(col_widths[0], 5, time, border=0, fill=True, align='C')

        # Topic column
        self.set_xy(x_start + col_widths[0], y_before)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(248, 249, 250)
        self.multi_cell(col_widths[1], 5, topic, border=0, fill=True)

        # Activity column
        self.set_xy(x_start + col_widths[0] + col_widths[1], y_before)
        self.set_font('Helvetica', '', 7)
        self.multi_cell(col_widths[2], 5, activity, border=0)

        # Resource column
        self.set_xy(x_start + col_widths[0] + col_widths[1] + col_widths[2], y_before)
        self.set_font('Helvetica', 'I', 6)
        self.set_text_color(99, 110, 114)
        self.multi_cell(col_widths[3], 5, resource, border=0)

        y_after = self.get_y()
        line_height = max(y_after - y_before, 10)

        # Draw borders
        self.set_draw_color(200, 200, 200)
        for i, w in enumerate(col_widths):
            x = x_start + sum(col_widths[:i])
            self.rect(x, y_before, w, line_height)

        self.set_y(y_before + line_height)

    def milestone(self, text):
        self.set_fill_color(255, 243, 205)
        self.set_draw_color(255, 193, 7)
        x = self.get_x()
        y = self.get_y()
        self.rect(x, y, 267, 10, 'DF')
        self.set_xy(x + 3, y + 2)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(133, 100, 4)
        self.multi_cell(260, 4, text)
        self.set_y(y + 12)

    def tips_section(self):
        self.add_page()
        self.set_fill_color(9, 132, 227)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, '  Daily Tips for Success', new_x='LMARGIN', new_y='NEXT', fill=True)
        self.ln(3)

        tips = [
            'Code every day - consistency beats cramming. Type all code manually.',
            'Use the Pomodoro technique - 50 min focus + 10 min break during study blocks.',
            'Build projects - they matter more than certificates for job applications.',
            'Use Anki/flashcards - for SQL syntax, Pandas methods, and ML concepts.',
            'Join communities - r/datascience, Kaggle forums, Discord servers for support.',
            'Teach what you learn - write blog posts or explain concepts to reinforce learning.',
            'Track progress - maintain a learning journal or GitHub commit history.'
        ]

        for tip in tips:
            self.set_text_color(0, 0, 0)
            self.set_font('Helvetica', '', 8)
            self.cell(5, 6, chr(149), new_x='END')
            self.multi_cell(0, 6, tip)
            self.ln(1)

    def resources_section(self):
        self.add_page()
        self.set_fill_color(45, 52, 54)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, '  Recommended Free Resources', new_x='LMARGIN', new_y='NEXT', fill=True)
        self.ln(3)

        resources = [
            ('Python', 'Automate the Boring Stuff', 'automatetheboringstuff.com'),
            ('Python', 'Python Crash Course (Book)', 'nostarch.com/pythoncrashcourse2e'),
            ('SQL', 'SQLBolt', 'sqlbolt.com'),
            ('SQL', 'Mode SQL Tutorial', 'mode.com/sql-tutorial'),
            ('Pandas', 'Kaggle Pandas Course', 'kaggle.com/learn/pandas'),
            ('Pandas', '10 Minutes to Pandas', 'pandas.pydata.org/docs'),
            ('NumPy', 'NumPy Quickstart', 'numpy.org/doc/stable'),
            ('ML', 'Google ML Crash Course', 'developers.google.com/machine-learning/crash-course'),
            ('ML', "Andrew Ng's ML Specialization", 'coursera.org/specializations/machine-learning-introduction'),
            ('Practice', 'LeetCode (Python)', 'leetcode.com'),
            ('Practice', 'HackerRank SQL', 'hackerrank.com/domains/sql'),
            ('Practice', 'Kaggle', 'kaggle.com'),
        ]

        self.set_font('Helvetica', 'B', 8)
        self.set_fill_color(223, 230, 233)
        self.cell(30, 7, 'Topic', border=1, fill=True, align='C')
        self.cell(80, 7, 'Resource', border=1, fill=True, align='C')
        self.cell(80, 7, 'Link', border=1, fill=True, align='C')
        self.ln()

        self.set_font('Helvetica', '', 7)
        for topic, resource, link in resources:
            if self.get_y() > 185:
                self.add_page()
                self.set_font('Helvetica', 'B', 8)
                self.set_fill_color(223, 230, 233)
                self.cell(30, 7, 'Topic', border=1, fill=True, align='C')
                self.cell(80, 7, 'Resource', border=1, fill=True, align='C')
                self.cell(80, 7, 'Link', border=1, fill=True, align='C')
                self.ln()
                self.set_font('Helvetica', '', 7)

            self.set_fill_color(248, 249, 250) if resources.index((topic, resource, link)) % 2 == 0 else self.set_fill_color(255, 255, 255)
            self.cell(30, 6, topic, border=1, fill=True, align='C')
            self.cell(80, 6, resource, border=1, fill=True)
            self.cell(80, 6, link, border=1, fill=True)
            self.ln()


def main():
    pdf = PDF()
    pdf.alias_nb_pages()

    # Page 1: Overview + Phase 1
    pdf.add_page()

    # Phase overview boxes
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, 'Phase Overview:', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(2)

    y_start = pdf.get_y()
    pdf.phase_box('Phase 1', 'Weeks 1-2', 'Python Fundamentals', (17, 153, 142))
    pdf.phase_box('Phase 2', 'Weeks 3-4', 'SQL & Databases', (79, 172, 254))
    pdf.phase_box('Phase 3', 'Weeks 5-6', 'Pandas & NumPy', (250, 112, 154))
    pdf.phase_box('Phase 4', 'Weeks 7-8', 'Machine Learning', (161, 140, 209))
    pdf.set_y(y_start + 20)

    # Week 1
    pdf.section_title('Week 1: Python Basics', 'Phase 1 - Python Fundamentals')
    pdf.day_row('9:00-10:30', 'Variables & Data Types', 'Learn int, float, str, bool. Practice type conversion and string formatting.', 'Python.org Tutorial')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Strings Deep Dive', 'Slicing, methods (split, join, replace, strip), f-strings. Solve 10 string problems.', 'W3Schools Python')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Lists, Tuples & Sets', 'Operations, methods, differences. Practice with 15 list exercises.', 'Automate Boring Stuff')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Dictionaries', 'Key-value pairs, nesting, iteration. Build a phonebook app.', 'Python Crash Course')
    pdf.ln(3)

    # Week 2
    pdf.section_title('Week 2: Intermediate Python', 'Phase 1 - Python Fundamentals')
    pdf.day_row('9:00-10:30', 'Conditionals & Logic', 'if/elif/else, comparison & logical operators. Solve 20 conditional problems.', 'HackerRank Python')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Loops (for & while)', 'break, continue, nested loops, range(). Solve 25 loop problems.', 'LeetCode Easy')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Functions', 'Parameters, return values, scope, *args, **kwargs, lambda. Write 10 functions.', 'Python Crash Course')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Comprehensions & File I/O', 'List/dict comprehensions, reading/writing files, error handling (try/except).', 'Automate Boring Stuff')
    pdf.milestone('MILESTONE: Build a CLI mini-project (To-Do List or Quiz Game) using all Week 1-2 concepts.')

    # Week 3
    pdf.section_title('Week 3: SQL Fundamentals', 'Phase 2 - SQL & Databases')
    pdf.day_row('9:00-10:30', 'DB Basics & SELECT', 'Relational DB concepts, tables/rows/columns. Practice SELECT, FROM, WHERE.', 'SQLBolt Lesson 1-3')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Filtering & Sorting', 'ORDER BY, LIMIT, DISTINCT, AND/OR/NOT, BETWEEN, LIKE, IN.', 'SQLBolt Lesson 4-6')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Aggregate Functions', 'COUNT, SUM, AVG, MIN, MAX. GROUP BY, HAVING. Solve 20 aggregation queries.', 'Mode SQL Tutorial')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Practice & Challenges', 'Complete 30 SQL queries on sample datasets (Chinook DB, Employees DB).', 'HackerRank SQL')
    pdf.ln(3)

    # Week 4
    pdf.section_title('Week 4: Advanced SQL + Python Integration', 'Phase 2 - SQL & Databases')
    pdf.day_row('9:00-10:30', 'JOINs', 'INNER, LEFT, RIGHT, FULL JOIN. Visualize joins, solve 15 join problems.', 'SQLBolt Lesson 7-9')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Subqueries & CTEs', 'Nested queries, WITH clause, correlated subqueries.', 'Mode SQL Tutorial')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Window Functions', 'ROW_NUMBER, RANK, DENSE_RANK, PARTITION BY, running totals.', 'PostgreSQL Tutorial')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Python + SQL', 'sqlite3 library, SQLAlchemy ORM. Build a Python app that queries a database.', 'Real Python SQLite')
    pdf.milestone('MILESTONE: Query a real dataset (Kaggle Titanic) using both SQL and Python. Complete 50+ SQL queries.')

    # Week 5
    pdf.section_title('Week 5: NumPy', 'Phase 3 - Pandas & NumPy')
    pdf.day_row('9:00-10:30', 'NumPy Arrays', 'Creating arrays, vs Python lists, data types, shape, reshape.', 'NumPy Quickstart')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Indexing & Slicing', '1D/2D/3D indexing, boolean masking, fancy indexing.', 'NumPy Documentation')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Broadcasting & ufuncs', 'Universal functions, vectorized operations, broadcasting rules.', 'Python Data Science Handbook')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Linear Algebra & Random', 'Dot product, matrix ops, random number generation, seeding.', 'Kaggle NumPy Course')
    pdf.ln(3)

    # Week 6
    pdf.section_title('Week 6: Pandas', 'Phase 3 - Pandas & NumPy')
    pdf.day_row('9:00-10:30', 'Series & DataFrames', 'Creating, head(), info(), describe(), dtypes, shape.', 'Kaggle Pandas Course')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Selecting & Filtering', 'loc[], iloc[], boolean filtering, query(), isin().', '10 Minutes to Pandas')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Missing Data & groupby', 'fillna(), dropna(), groupby(), agg(), pivot_table().', 'Pandas Documentation')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Merging, Joining & Dates', 'merge(), concat(), join(), datetime handling, apply(), map().', 'Python Data Science Handbook')
    pdf.milestone('MILESTONE: Complete a full EDA project on any Kaggle dataset using Pandas + NumPy.')

    # Week 7
    pdf.section_title('Week 7: ML Foundations', 'Phase 4 - Machine Learning')
    pdf.day_row('9:00-10:30', 'ML Intro & Types', 'Supervised vs Unsupervised, regression vs classification, ML workflow.', 'Google ML Crash Course')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Train-Test Split & Overfitting', 'Splitting data, cross-validation, bias-variance tradeoff.', 'Scikit-learn Docs')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Linear Regression', 'Theory + implementation with scikit-learn. Build first regression model.', 'Andrew Ng ML Course')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'Logistic Regression & Metrics', 'Classification, accuracy, precision, recall, F1-score, confusion matrix.', 'Google ML Crash Course')
    pdf.ln(3)

    # Week 8
    pdf.section_title('Week 8: Advanced ML + Final Project', 'Phase 4 - Machine Learning')
    pdf.day_row('9:00-10:30', 'KNN & Decision Trees', 'K-Nearest Neighbors, Decision Trees, Random Forests. Compare models.', 'Scikit-learn Tutorial')
    pdf.day_row('10:30-10:45', 'BREAK', 'Short break', '')
    pdf.day_row('10:45-12:30', 'Hyperparameter Tuning', 'GridSearchCV, RandomizedSearchCV, cross-validation strategies.', 'Kaggle ML Course')
    pdf.day_row('12:30-1:30', 'LUNCH', 'Lunch break', '')
    pdf.day_row('1:30-3:00', 'Feature Engineering & Scaling', 'Encoding, scaling (StandardScaler, MinMaxScaler), feature selection.', 'Feature Engineering')
    pdf.day_row('3:00-3:15', 'BREAK', 'Short break', '')
    pdf.day_row('3:15-5:00', 'FINAL PROJECT', 'End-to-end ML project: dataset > EDA > clean > model > evaluate > present.', 'Kaggle Competitions')
    pdf.milestone('FINAL MILESTONE: Complete an ML portfolio project. Write project summary, update GitHub & resume.')

    # Tips and Resources
    pdf.tips_section()
    pdf.resources_section()

    # Output
    output_path = r'C:\Users\GATEW\OneDrive\Documents\Default Project\Data_Science_Timetable_8Weeks.pdf'
    pdf.output(output_path)
    print(f'PDF generated: {output_path}')

if __name__ == '__main__':
    main()