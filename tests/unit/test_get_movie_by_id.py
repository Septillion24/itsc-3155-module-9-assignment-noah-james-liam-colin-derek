def test_get_movie_by_id(self):
    # Success condition
    movie = self.repo.create_movie("Test Movie", "Test Director", 5)
    retrieved_movie = self.repo.get_movie_by_id(movie.id)
    self.assertEqual(movie, retrieved_movie)

    # Fail condition: 
    non_existing_id = -1
    with self.assertRaises(Exception): #idk what exception you raise
        self.repo.get_movie_by_id(non_existing_id)
