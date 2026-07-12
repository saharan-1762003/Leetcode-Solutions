class Solution {
private:
    void dfs(int row, int col, vector<vector<int>>& image,
             int initialColor, int newColor) {

        int n = image.size();
        int m = image[0].size();

        image[row][col] = newColor;

        int delrow[] = {-1, 0, 1, 0};
        int delcol[] = {0, 1, 0, -1};

        for(int i = 0; i < 4; i++){
            int nrow = row + delrow[i];
            int ncol = col + delcol[i];

            if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
               image[nrow][ncol] == initialColor &&
               image[nrow][ncol] != newColor) {
                
                dfs(nrow, ncol, image, initialColor, newColor);
            }
        }
    }

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image,
                                  int sr, int sc, int color) {
        
        int initialColor = image[sr][sc];

        if(initialColor == color) return image;

        dfs(sr, sc, image, initialColor, color);
        return image;
    }
};