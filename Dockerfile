FROM ubuntu
RUN apt update -y
RUN apt install wget unzip file libcurl4 -y
RUN wget -qO /tmp/server "https://github.com/QW-Group/mvdsv/releases/latest/download/mvdsv_linux_amd64"

RUN mkdir -p /quake/id1/maps

WORKDIR /tmp
RUN wget -qO /tmp/qwprogs.zip "https://github.com/QW-Group/ktx/releases/latest/download/qwprogs-linux-amd64.zip"

RUN mv /tmp/qwprogs.zip /quake/id1
WORKDIR /quake
RUN unzip /quake/id1/qwprogs.zip
RUN mv /quake/qwprogs.so /quake/id1/qwprogs.so

#LOWERCASE PAK NEEDED BECAUSE LINUX!!

COPY ./id1/pak* /quake/id1
COPY ./id1/server.cfg /quake/id1
COPY ./id1/maps /quake/id1/maps

RUN mv /tmp/server /quake
RUN chmod +x /quake/server

EXPOSE 27500/UDP

CMD ["/quake/server"]