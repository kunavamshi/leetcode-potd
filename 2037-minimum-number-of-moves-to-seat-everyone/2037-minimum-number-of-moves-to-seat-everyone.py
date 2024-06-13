class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both lists
        seats.sort()
        students.sort()
        
        # Initialize total moves counter
        total_moves = 0
        
        # Sum the absolute differences between paired seats and students
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        
        return total_moves