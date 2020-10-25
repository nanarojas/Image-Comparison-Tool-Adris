FROM python:3.8
LABEL MAINTAINER Adriana Rojas ad.rojasvo@gmail.com
# Utils required for image processing
RUN apt-get update \
  && apt install -y libgl1-mesa-glx
ADD images /sre/images/
ADD images_to_compare.csv /sre/
ADD requirements.txt /sre/
RUN pip install -r /sre/requirements.txt
ADD image_diff_score.py /sre/
ADD expected_results.csv /sre/
ADD test.sh /sre
ADD cli.py /sre/
RUN /sre/test.sh
ENTRYPOINT ["/sre/cli.py"]
# TODO: Drop privileges
