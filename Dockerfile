FROM alpine

COPY ./workhours /home/workhours

RUN chmod 777 -R /home/workhours

WORKDIR /home/workhours

ENTRYPOINT ["./workhours"]

CMD [""]