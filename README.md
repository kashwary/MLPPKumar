# MLPPKumar

Initially I used found a datacamp video explaining how to do a API call to import data. After that I used the documentation from ACS website as I was not able to get the block level data pulled using that video. 
I tried a bunch of variables ranging from different population for different race to age and sex. A bunch of them didn't have the value for block level data. After trying for a bunch variables I chose, total population followed by male and female split for the total population. The other variables in the dataset are state, block, county.
When importing it and creating a dataframe using the data, i renamed the columns and switched from Pennsylvania state to Alaska. The data for Pennsylvania was a bit big and hearing from other students reporting that it took time for them to push the data onto postgres I changed it to Alaska. 
To push the data from a csv to postgres sql I used this resource (https://www.dataquest.io/blog/loading-data-into-postgres/) to push the data to the server. One thing that we had to do was to commit changes to the server and I was stuck at it as I couldn't see my table in the database. 
I followed this up with creating a repository on my system first and then pushing the changes in my python files to the githib repository. I used this ( https://www.datacamp.com/community/tutorials/git-push-pull) resource to push the data. 
