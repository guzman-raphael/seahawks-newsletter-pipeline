FROM ubuntu:jammy 
ENV TEAM="Seahawks"
COPY ./README.md /home/ubuntu/files/README.md
ADD https://raw.githubusercontent.com/datajoint/datajoint-python/master/CHANGELOG.md /home/ubuntu/files/CHANGELOG.md
RUN echo HEY! > /home/ubuntu/files/file1.txt
USER games:games
ENTRYPOINT ["bash", "-c"]
CMD ["tail -f /dev/null"] 
