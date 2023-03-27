d1 = {'term': '23t1', 'course_metadata': {'foundation': {'hs1002': 'Jan 2023 - English II', 'ma1003': 'Jan 2023 - Mathematics II', 'ma1004': 'Jan 2023 - Statistics II', 'cs1002': 'Jan 2023 - Python'}, 'degree': {'gn3001': 'Jan 2023 - Strategies for Professional Growth', 'cs3001': 'Jan 2023 - Software Engineering'}, 'diploma': {'se2002': 'Jan 2023 - TDS', 'cs2007': 'Jan 2023 - MLT', 'cs2004': 'Jan 2023 - ML Foundations', 'ms2001': 'Jan 2023 - BDM', 'ms2002': 'Jan 2023 - BA', 'cs2008': 'Jan 2023 - MLP', 'se2001': 'Jan 2023 - System Commands', 'cs2006': 'Jan 2023 - MAD II', 'ma2001': 'Jan 2023 - Linear Statistical Models', 'cs2005': 'Jan 2023 - JAVA', 'cs2003': 'Jan 2023 - MAD I', 'cs2002': 'Jan 2023 - PDSA', 'cs2001': 'Jan 2023 - DBMS'}}, 'prefix': 'ns'}

d2 = {'term': '23q1', 'course_metadata': {'foundation': {'cs1001': 'Jan Qualifier - 2023: CT', 'ma1002': 'Jan Qualifier - 2023: Statistics I', 'hs1001': 'Jan Qualifier - 2023: English I', 'ma1001': 'Jan Qualifier - 2023: Mathematics I'}}, 'prefix': 'ns'}

d1['course_metadata']['foundation'].update(d2['course_metadata']['foundation'])

print(d1)