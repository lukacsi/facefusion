# Intro
We are trying to revamp the processing of steps to streamline the process of jobs.

Currently a job step always splits the source video into frames, runs the step's processors on it then merges the frames. The problem is when we run a job with multiple remix steps, the video gets processed unessesary amount of times this costs a lot of processing power and time and also causes the resulting video to be compressed multiple times.

### job step vs job remix step
The difference between the two is that if you run multiple faceswaps (using this processor for eplanation), and you them as multiple steps, you get separate videos of each face. If you swap a face using step, and then the rest using remix step, the steps get piped into eachother.

step output -> remix step 1 input -processing- remix 1 step output -> remix step 2 input ....etc

# Process
* flag jobs that only contain a first normal step, and one or more subsequent remix steps.
* flag the first, middle and last steps if the job satisfies the first flag.
* skip merging and extracting frames based on flags, first => no merge, middle => no merge, no extract, last => no extract.
* change the step procession pipeline to work with directories containing frames instead of a single image/video.
* test

# Misc
I have gone and commented some of the functions and lines that I deemed the most relevant to help in picking up the fork.
