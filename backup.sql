PGDMP                         {            mentor    14.8    14.8     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    97768    mentor    DATABASE     c   CREATE DATABASE mentor WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE mentor;
                postgres    false            �            1259    97770    messages    TABLE     �   CREATE TABLE public.messages (
    id integer NOT NULL,
    message_type character varying(2000) NOT NULL,
    content text NOT NULL
);
    DROP TABLE public.messages;
       public         heap    postgres    false            �            1259    97769    messages_id_seq    SEQUENCE     �   CREATE SEQUENCE public.messages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.messages_id_seq;
       public          postgres    false    210            �           0    0    messages_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.messages_id_seq OWNED BY public.messages.id;
          public          postgres    false    209            \           2604    97773    messages id    DEFAULT     j   ALTER TABLE ONLY public.messages ALTER COLUMN id SET DEFAULT nextval('public.messages_id_seq'::regclass);
 :   ALTER TABLE public.messages ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210            �          0    97770    messages 
   TABLE DATA           =   COPY public.messages (id, message_type, content) FROM stdin;
    public          postgres    false    210   p
       �           0    0    messages_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.messages_id_seq', 1, true);
          public          postgres    false    209            ^           2606    97777    messages messages_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.messages DROP CONSTRAINT messages_pkey;
       public            postgres    false    210            �   `  x��Z[o�~&�6@��iɒ|'i�Pm�ɀ ɔ��JNbt1%%r�Ĉ� �k�/�KQ�䒫��/��G��f��Y��Q�Ƚ�3�o�������Rm���Jw�(i&a�W
����^��/��_�^2�r#��(&1}�&�t/}r�x����V�>(�moon]�x�ν���GKw*_�W������..~�2�ۯ��_ݼ���O�W
_�U�j��GՇ���� �g&=��")h��Y2L��A����cҦ]�F��ҵ],��=.��~)H��,=&Yi��ޑG�B/=a�Rs�>�;I��<�U��n��	�4du���oD�>���CZ1LαfӞ�5�� ������r��������g����m�x[HOK�
q�O��:!���lb�[��iFf�g6ۃ��`�_`�ѳ��09�~��G~h`ף jt�5�����C���-`�lv��J�iɬ䝗�4iE���?B6
�1:�I�O|;�Z�Jyr��
KA�=�=�0��=�>f�άU�]���*6�@ȝ을S<O/���
~�6pdak����nB�/�bw��:���'َhu
�$���!V�ԣp�"�"z=�&.�(Ρ}�@6��%��s8�LG�Â��{(ژȍ ���
5��{���`�(���.����3�J�V��� D$�JBJ=��Ɗ��S Gz46���q�f{!E���iM�\qv��Uy�z�2sj	o��n~~kq��'�3���U�2���������j�N�aS��j�!���H`��34���0����ۯ�(ɳ��"�1����֯�+)���ޘ��H1��e�$��8�h���%
҉�������C O������v5��cz)�"�i��E�f�Y��ƒ0g���Y*�@2�z�/�i��y?����q��Jd�SD�.����R�A�� �� ��)���R��	����)~5�o��C�^�hnH���2���$�e~D�t�tFD uI��a�4q�Ņ�z�V��H��gY)����<���,�E0A��M/Q��t����n�jjeAENn�V�;�Py�Y�] �P�=*$?#{�,�sZ�%��B�6@��xe�`��N�LDN� �63��$���WƓW;�E�A��)�m�@!�M�"��O�
 +!�@�_��
?��B���\C�oXno��`�]6����
�c|���f�W�Z
�BtP`�*�{�?�TOa�{+D;'��U��;,aI�nI����ٗ*g|Z#��mj�\���
�y�� W�/�F-��Wfᜭ�tŸt��k�j��~Gn �#d�1v����`>�?�b{�Z
ޜ"H�7G��j��
�d̏��HP,�����H�&�X ��ÙɁX�x§^�:,�� ��M�bvrR1�4���m6�O0,"��Y�}27Jc��L<�Y�Hr�~��H�]��'8��>	�5�^Q���%��V��N^������D��Q��S���P.�L��#⎷EA�ʸ�I����Pg���L�PǼ��,Æd���ˀ�1�jTxO+XA�
�|� �ȸNf�('b�L����#�
�q�W
-#�u%\Υ��hc�D[􅚧�6=�B\�
���!�*�cz-aI;�I�&��7��b�ڟZ����.���-�zl&�4�J�vV����ii�侗\��EaGC��-I>y@�� ͎�1v���=�y�|~�ɡWK��@�XQ	]Z7"or���H�U��x�o�����e�`SA�\/ �i�X �����̅�Х3?��R���hN�t,�֪��D5r�)+��SiJ��hFV�I+���W�I��c��\�w���&���Ow �r��Fr�Ηc	�1 r�d�򔱜�2$`�ʕ�H�]G��x��c�kpr��:�g����+A������C�?ݬUD`X[-Մ����+َ-1a��0W&�p��*��=�eK�@�JX���ud�g�\b x�H@\�p�n$s]T���8�����Zk�T�I���h�=�s���@�|L���Hx�yF3@T�)�@D�L�yYXFK:�1b溲af6τh��^.����9AbO�3܃d���dc�a���\@"��KFXvO��b`.�Y��͑�3�S��&t}����P�}<��uY}����
�o�Z�̹��ͧ� ?}va ԙ	�����m:��t�x�P)�J�t���=^Nm�sQ�8C�
A�l}I�\
�ǢG[���<b��g�pa�n�dH6���	^�C�� =u�I��DQ6"�/_e8���Q��P��	�myd �-���}G-��pZҕ�aڊ����F��?��%��#�lS��i;�WA�=����&i���"�BiZ�;7��z�&9r4�F�rQ�Wc!�f֡���U��O���X
D��4�&�[,�U+��Jd-�c_c�1ܲ��x37�P�: o��i�Z%�e�L#m����Nԃ�V[�!�Xv���hcx��m�W�\d�l�2ۘq0�Q"�ed^��������!�ЫX�Wdk�]VK��Μ�?O��Kۋ�w�sϳ��o�� �>fn�7�2�z�7��kЙ�be��du�iL��e�.�HG�bF)X~A2�����\*�xI+E�i��f(2pj���{�����i6]�|�z8TXc�y�d�ӝ�����=䷐���3�I�{G���BY��_yJ�ل�'*�7�0�d�<�z������#��H��a �ƭw�I^4��
G�io>hZ/�����I�g�O�������y7�`�N?�S�k?��Y�B�<Jd���y��j��;����юFG�}���ـDv�c��H���@䚌��9i�8�@v�2NҦ���oNa'=KV�$�������|�ν��J���R)���ɐ�ͽ)RE$�nz�N?tKr��zya��b��:cP�3�aQn\Ar�d�糦Pr1��Z*��Wʌ��z���8�ĸ
�'`��h�m��1v���u�Iz�"��,�"DΓ�1-7����oS9��:y�G(��G� ���2p,,�Oc
c=�Ȧ-LU��M���$ypf��dɑ!�=�֒�� ��9�����7�������b��P�l��}����:;DY�B4dC��Y[|)���C�~\|�y�s��v9�g@�o��9�����n_w��@�g[��;᩼G��X�BAE@�{"���d�����S��5C�O-�w$�n�|"�Ӱz��ޜ���8�ϡ�R�0xOb�N#<�FU�Hh�*vM�\h��7�yBB�������(zWD����Rl��5���J�g:8��si����|� r�i��L�'���V��(�#u��Ӷ6�PW�<����Ky��1�q���x�v�U�~x�"�v�{}��y&m%�G\Ƒ��ϵ�z����Z�>~K���ҽ׃/�]�6���}Fq�r�V�z����cm��!W�_Vjە���ƿ�4��/��yl�����;�7ז��n�,���ͯ����,_Z�Z�4733w�rgvu�����+s���|��h�r�^�pmm{�V�am�rC$���Ԫ��}�������r�X�u��     