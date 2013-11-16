FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/explore/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/ExploreState.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ExploreState.lisp"
  "../msg_gen/lisp/ExploreFeedback.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ExploreFeedback.lisp"
  "../msg_gen/lisp/ExploreGoal.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_ExploreGoal.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
