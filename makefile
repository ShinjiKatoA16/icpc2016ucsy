CC = gcc
CFLAGS = $(shell pkg-config --cflags glib-2.0) -g -O0
LDLIBS = $(shell pkg-config --libs glib-2.0)
