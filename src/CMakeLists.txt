add_executable(hello
	main.cpp
)

install(TARGETS hello DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
