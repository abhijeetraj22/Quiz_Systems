import sqlite3


def checkSetup():
    conn = sqlite3.connect('Quiz_System.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='admin_detail'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True


def setup():
    conn = sqlite3.connect('Quiz_System.db')
    cursor = conn.cursor()
    create_admin_table = """
        CREATE TABLE admin_detail (
    admin_id       INTEGER       PRIMARY KEY AUTOINCREMENT
                                 UNIQUE
                                 NOT NULL,
    admin_name     VARCHAR (40)  NOT NULL,
    admin_gender   VARCHAR (5)   NOT NULL,
    admin_email    VARCHAR (40)  NOT NULL
                                 UNIQUE,
    admin_mobile   VARCHAR (11)  NOT NULL,
    admin_password VARCHAR (50)  NOT NULL,
    admin_sec_ques VARCHAR (100),
    admin_sec_ans  VARCHAR (50) 
);
    """
    create_quiz_table = """
        CREATE TABLE quiz_detail (
    quiz_id          INTEGER      PRIMARY KEY
                                  UNIQUE
                                  NOT NULL,
    quiz_name        VARCHAR (50) NOT NULL
                                  UNIQUE,
    quiz_time_limit  INTEGER      NOT NULL,
    quiz_per_qs_mark INTEGER      NOT NULL,
    quiz_attempt_qs  INTEGER      NOT NULL,
    quiz_total_ques  INTEGER      NOT NULL,
    admin_id         INTEGER      REFERENCES admin_detail (admin_id) ON DELETE NO ACTION
                                                                     ON UPDATE NO ACTION
                                                                     MATCH [FULL]
                                  NOT NULL
);

    """
    create_quiz_question_table = """
        CREATE TABLE quiz_question (
    ques_no  INTEGER        PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
    question VARCHAR (3000) NOT NULL,
    opa      VARCHAR (100)  NOT NULL,
    opb      VARCHAR (100)  NOT NULL,
    opc      VARCHAR (100)  NOT NULL,
    opd      VARCHAR (100)  NOT NULL,
    answer   INTEGER        NOT NULL,
    quiz_id  INTEGER        REFERENCES quiz_detail (quiz_id) ON DELETE CASCADE
                                                             ON UPDATE CASCADE
                                                             MATCH [FULL]
                            NOT NULL
);
    """
    create_user_table = """
CREATE TABLE user_detail (
    user_id       INTEGER       PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
    user_name     VARCHAR (40)  NOT NULL,
    user_gender   VARCHAR (5)   NOT NULL,
    user_email    VARCHAR (40)  NOT NULL
                                UNIQUE,
    user_mobile   VARCHAR (11)  NOT NULL,
    user_city     VARCHAR (40)  NOT NULL,
    user_state    VARCHAR (40)  NOT NULL,
    user_country  VARCHAR (40)  NOT NULL,
    user_password VARCHAR (100) NOT NULL,
    user_sec_ques VARCHAR (100) NOT NULL,
    user_sec_ans  VARCHAR (50)  NOT NULL
);
    """
    create_result_table = """
CREATE TABLE user_result (
    user_id     INTEGER REFERENCES user_detail (user_id) ON DELETE NO ACTION
                                                         ON UPDATE NO ACTION
                                                         MATCH [FULL]
                        NOT NULL,
    quiz_id     INTEGER REFERENCES quiz_detail (quiz_id) ON DELETE NO ACTION
                                                         ON UPDATE NO ACTION
                                                         MATCH [FULL]
                        NOT NULL,
    attempt     INTEGER NOT NULL,
    score       INTEGER NOT NULL,
    total_score INTEGER NOT NULL
);
    """
    create_question_trigger = """
    CREATE TRIGGER delete_question_trig
        BEFORE DELETE
            ON quiz_detail
      FOR EACH ROW
BEGIN
    DELETE FROM quiz_question
          WHERE quiz_id = old.quiz_id;
END
        """
    create_result_trigger = """
    CREATE TRIGGER delete_result_trig
        BEFORE DELETE
            ON quiz_detail
      FOR EACH ROW
BEGIN
    DELETE FROM user_result
          WHERE quiz_id = old.quiz_id;
END;
        """

    cursor.execute(create_admin_table)
    cursor.execute(create_quiz_table)
    cursor.execute(create_quiz_question_table)
    cursor.execute(create_user_table)
    cursor.execute(create_result_table)
    cursor.execute(create_question_trigger)
    cursor.execute(create_result_trigger)
    conn.commit()
    conn.close()


def getConnection():
    return sqlite3.connect('Quiz_System.db')
