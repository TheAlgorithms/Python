ifeq (${IMAGE_NAME}, )
	IMAGE_NAME=devcontainer
endif
ifeq (${IMAGE_VERSION}, )
	IMAGE_VERSION=latest
endif
ifeq (${WORK_DIR}, )
	WORK_DIR=work-dir
endif


default: build

build:
	docker build -t ${IMAGE_NAME}\:${IMAGE_VERSION} -f dockerfile .

setup-env:
	docker run -it -v ${ABSOLUTE_PATH_TO_WORKDIR}\:/${WORKDIR} ${IMAGE_NAME}\:${IMAGE_VERSION} bash

cleanup:
	docker rmi -f ${IMAGE_NAME}\:${IMAGE_VERSION}
