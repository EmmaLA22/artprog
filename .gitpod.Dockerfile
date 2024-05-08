FROM gitpod/workspace-full
USER gitpod

RUN pip install pandas seaborn scikit-learn kneed 

git pull origin master  
