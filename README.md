# radiation-monitoring-system-1
crate files called app and mitigations:
mkdir app 
mkdir migrations
cd app
I created another files 
type nul > Dockerfile
type nul > Cloudbuild.yaml
type nul > start-script.sh
I did commit "chore: add base project structure"
git push


 create mode 100644 Dockerfile
 create mode 100644 app/main.py
 create mode 100644 app/requirements.txt
 create mode 100644 cloudbuild.yaml
 create mode 100644 migrations/001_create_table.sql
 create mode 100644 startup-scrip.sh

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 560 bytes | 24.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Azharelly/radiation-monitoring-system-1.git
   464fc3a..34c6b84  main -> main

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>cd app

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1\app>cd main.py
The directory name is invalid.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1\app>feat: add basic 
Flask API with sample endpoints 
'feat:' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1\app>
C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1\app>cd..

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>feat: add basic Flas
k API with sample endpoints
'feat:' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git commit -m "feat: add basic Flask API with sample endpoints"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app/main.py
        modified:   app/requirements.txt
        deleted:    startup-scrip.sh

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        startup-script.sh

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git push
Everything up-to-date

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git commit -m "feat: add basic Flask API with sample endpoints"
[main 63f205c] feat: add basic Flask API with sample endpoints
 3 files changed, 32 insertions(+)
 rename startup-scrip.sh => startup-script.sh (100%)

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git push
Enumerating objects: 9, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 998 bytes | 249.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Azharelly/radiation-monitoring-system-1.git
   34c6b84..63f205c  main -> main

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git add migrations/001_create_table.sql

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git commit -m "feat: add initial SQL migration for radiations_logs table"
[main f808559] feat: add initial SQL migration for radiations_logs table
 1 file changed, 6 insertions(+)

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 509 bytes | 169.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Azharelly/radiation-monitoring-system-1.git
   63f205c..f808559  main -> main

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>
 *  History restored 

Microsoft Windows [Version 10.0.26100.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>
 *  History restored 

Microsoft Windows [Version 10.0.26100.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>




Microsoft Windows [Version 10.0.26100.7171]
Microsoft Windows [Version 10.0.26100.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git add app/main.py app/requirements.txt

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git commit -m "feat: prepare Flask app for Cloud SQL connection using env variables"
[main 754a20f] feat: prepare Flask app for Cloud SQL connection using env variables
 1 file changed, 31 insertions(+), 10 deletions(-)

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 945 bytes | 472.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Azharelly/radiation-monitoring-system-1.git
   f808559..754a20f  main -> main

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>type nul > .env

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\Users\azhar\OneDrive\Desktop\Cloud CA - 1\radiation-monitoring-system-1>
I created the trigger to be able to do the push automatic and I liked my git and the project 