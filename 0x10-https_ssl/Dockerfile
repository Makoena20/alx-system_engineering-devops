FROM haproxy:latest

# Copy the haproxy configuration file
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

# Run HAProxy
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

