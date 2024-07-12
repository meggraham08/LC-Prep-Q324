class Solution:
    def minimumAverage(self, arr: List[int]) -> float:

        if not arr:
            return []  # Return an empty list if the array is empty

        averages = []

        while len(arr) > 1:
            left = 0
            right = len(arr) - 1

            smallest = float('inf')
            largest = float('-inf')

            # Find smallest and largest elements
            while left <= right:
                if arr[left] < smallest:
                    smallest = arr[left]
                if arr[left] > largest:
                    largest = arr[left]
                
                if arr[right] < smallest:
                    smallest = arr[right]
                if arr[right] > largest:
                    largest = arr[right]
                
                # Move pointers towards each other
                left += 1
                right -= 1

            # Remove the smallest and largest elements from the array
            arr.remove(smallest)
            arr.remove(largest)

            # Add the smallest and largest elements together
            total = smallest + largest

            # Calculate the average of the sum
            average = total / 2

            # Append the average to the list of averages
            averages.append(average)

        smallest_average = min(averages) if averages else None


        return smallest_average

