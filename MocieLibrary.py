class MovieLibrary:
    def __init__(self, title = "None", rating = 0):
        movie = {"title": title, "rating": rating}
        self.movies = [movie]
    
    def add_movie(self, title, rating):
        try:
            if not isinstance(title, str) or not isinstance(rating, (int, float)):
                raise ValueError("Title must be a string and rating must be a number.")
            if rating < 0 or rating > 10:
                raise ValueError("Rating must be between 0 and 10.")
            movie = {"title": title, "rating": rating}
            self.movies.append(movie)
        except ValueError as e:
            print(f"Error adding movie: {e}")

    def get_average_rating(self, ratings):
        if not ratings:
            return 0
        sum = 0
        count = 0
        for rating in ratings:
            sum += rating
            count += 1
        return sum / count if count > 0 else 0
        
        
    def get_top_rated_movies(self, n):
        if n <= 0:
            return []
        sorted_movies = sorted(self.movies, key=lambda x: x['rating'], reverse=True)
        return sorted_movies[:n]
    
if __name__ == "__main__":
    library = MovieLibrary()
    library.add_movie("Inception", 8.8)
    library.add_movie("The Matrix", 8.7)
    library.add_movie("Interstellar", 8.6)
    
    print("Top rated movies:")
    for movie in library.get_top_rated_movies(3):
        print(f"{movie['title']} - Rating: {movie['rating']}")
    
    ratings = [movie['rating'] for movie in library.movies]
    print(f"Average rating: {library.get_average_rating(ratings)}")