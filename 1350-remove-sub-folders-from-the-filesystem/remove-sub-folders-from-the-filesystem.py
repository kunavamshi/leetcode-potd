from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically
        folder.sort()
        result = []

        for f in folder:
            # Add the folder to result if it's not a subfolder of the last added folder
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result