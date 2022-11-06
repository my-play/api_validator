#https://www.linkedin.com/learning/unit-testing-in-python/running-pytest-with-docker?u=2162394
#https://docs.pytest.org/en/6.2.x/parametrize.html
#
# ---- how to use docker .
#

# to build (-t is image name, -f is Dockerfile path, . is the context folder)
# docker build -t test_api -f Dockerfile . --no-cache

# to run (-it is interactive terminal for colours etc, --name is the container nane, test_some_module is the image name)
# docker run -it --rm --name Timur-test2 test_api bash
# ./start-test.sh -->will run test and put result.xml to report folder.

