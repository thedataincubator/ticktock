test:
	PYTHONPATH=.:$PYTHONPATH py.test test

clean:
	find . | grep .py[co]$ | xargs rm -f

.PHONY: test
