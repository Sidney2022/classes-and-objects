
class Student:

	def __init__(self, name, age, tracks, score):
		self.name = name
		self.age = age
		self.tracks = tracks
		self.score = score

	def change_name(self, new_name):
		self.name = new_name
		print(new_name)

	def change_age(self, new_age):
		self.age = new_age
		print(new_age)

	def add_track(self, new_track):
		updated_tracks = self.tracks.copy()
		updated_tracks.append(new_track)
		print(updated_tracks)
		
	def get_score(self):
		print(self.score)
  

Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
