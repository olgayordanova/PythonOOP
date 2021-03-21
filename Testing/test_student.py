from student.project.student import Student
import unittest

class StudentTests(unittest.TestCase):

    def setUp(self):
        self.student = Student("Slavi")

    def test_student_initialized(self):
        self.assertEqual ( self.student.name, "Slavi" )
        self.assertEqual ( self.student.courses, {} )
        self.student.courses ={"Python": ["notes"]}
        self.assertEqual ( self.student.courses, {"Python":["notes"]} )

    def test_enroll_existing_course(self):
        self.student = Student ( "Slavi", {"Python":["notes"]})
        res = self.student.enroll ("Python", ["notes","notes2"], "ccc")
        self.assertEqual ( res, "Course already added. Notes have been updated." )

    def test_enroll_course_notes_y(self):
        res = self.student.enroll ("Python", ["notes","notes2"], "Y")
        self.assertEqual ( res, "Course and course notes have been added." )

    def test_enroll_course_notes_n(self):
        res = self.student.enroll ( "Python1", ["notes","notes2"], "" )
        self.assertEqual ( res, "Course and course notes have been added." )

    def test_enroll(self):
        # self.assertEqual ( self.student.enroll ( 'Python Basic', 'passed', "N" ),
        #                    "Course has been added." )
        # self.assertEqual ( self.student.courses, {'Python Basic': []} )

        res = self.student.enroll ( "python", "notes", "abs" )
        self.assertEqual ( res, "Course has been added." )
        self.assertEqual ( self.student.courses, {'python': []} )

    def test_add_notes(self):
        self.student = Student ( "Slavi", {"Python": ["notes"]} )
        res = self.student.add_notes( "Python","notes" )
        self.assertEqual ( res, "Notes have been updated" )

    def test_add_notes_raise_exp(self):
        self.student = Student ( "Slavi", {"Python": ["notes"]} )
        self.assertRaises ( Exception, self.student.add_notes, "Python1","notes1"  )

    def test_leave_existing_course(self):
        self.student = Student ( "Slavi", {"Python": ["notes"]} )
        res = self.student.leave_course ( "Python")
        self.assertEqual ( res, "Course has been removed" )

    def test_leave_not_existing_course(self):
        with self.assertRaises ( Exception ) as exp:
            self.student.leave_course("Python1")
        self.assertEqual ( exp.exception.args[0], "Cannot remove course. Course not found." )


if __name__ == "__main__":
    unittest.main ()